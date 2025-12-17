import pandas as pd
import numpy as np
import random
import os
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')
random.seed(42)
np.random.seed(42)

os.makedirs("data_sdr", exist_ok=True)

#SDRs

sdrs = [
    {"sdr_id": i, "nome": fake.name(), "experiencia_anos": random.randint(1, 5)}
    for i in range(1, 9)
]
df_sdrs = pd.DataFrame(sdrs)
df_sdrs.to_csv("data_sdr/sdrs.csv", index=False)

#Empresas

empresa_qtd = 5000
empresas = []

setores = ["SaaS", "Educação", "Saúde", "Indústria", "Varejo", "Financeiro", "Consultoria"]
tamanhos = ["ME", "EPP", "Médio", "Grande"]

for i in range(empresa_qtd):
    empresas.append({
        "empresa_id": i + 1,
        "nome_empresa": fake.company(),
        "setor": random.choice(setores),
        "tamanho": random.choice(tamanhos),
        "cnpj": fake.cnpj(),
        "cidade": fake.city(),
        "uf": fake.state_abbr(),
    })

df_empresas = pd.DataFrame(empresas)
df_empresas.to_csv("data_sdr/companies.csv", index=False)

#Leads

lead_qtd = 10000
origens = ["Inbound", "Outbound", "Indicação", "Eventos"]

leads = []

start_date = datetime(2023, 1, 1)

for i in range(lead_qtd):
    empresa_id = random.randint(1, empresa_qtd)
    created_at = start_date + timedelta(days=random.randint(0, 730))

    leads.append({
        "lead_id": i + 1,
        "nome": fake.name(),
        "email": fake.email(),
        "cargo": random.choice(["CTO", "CEO", "Gerente", "Analista", "Coordenador"]),
        "empresa_id": empresa_id,
        "origem": random.choice(origens),
        "criado_em": created_at,
        "sdr_owner": random.choice(df_sdrs["sdr_id"])
    })

df_leads = pd.DataFrame(leads)
df_leads.to_csv("data_sdr/leads.csv", index=False)

#Touchpoints

touchpoints = []
tipos_tp = ["Email", "Ligação", "WhatsApp", "LinkedIn"]

tp_id = 1
for lead in leads:
    tp_count = random.randint(1, 12)
    for _ in range(tp_count):
        tp_date = lead["criado_em"] + timedelta(days=random.randint(0, 30))
        touchpoints.append({
            "touchpoint_id": tp_id,
            "lead_id": lead["lead_id"],
            "sdr_id": lead["sdr_owner"],
            "tipo": random.choice(tipos_tp),
            "data": tp_date,
            "resultado": random.choice(["Sem resposta", "Interessado", "Não interessado"])
        })
        tp_id += 1

df_touchpoints = pd.DataFrame(touchpoints)
df_touchpoints.to_csv("data_sdr/touchpoints.csv", index=False)

# Oportunidades
opp = []
opp_id = 1

for lead in leads:
    # probabilidades realistas
    if np.random.rand() < 0.18:  # SQL
        if np.random.rand() < 0.10:  # Vira oportunidade
            valor = np.random.randint(2000, 80000)
            ganho = np.random.rand() < 0.22  # win rate

            opp.append({
                "opp_id": opp_id,
                "lead_id": lead["lead_id"],
                "empresa_id": lead["empresa_id"],
                "sdr_id": lead["sdr_owner"],
                "valor_previsto": valor,
                "valor_fechado": valor if ganho else 0,
                "status": "Ganhou" if ganho else "Perdeu",
                "data_criacao": lead["criado_em"] + timedelta(days=random.randint(5, 40)),
                "data_fechamento": lead["criado_em"] + timedelta(days=random.randint(20, 60))
            })

            opp_id += 1

df_opp = pd.DataFrame(opp)
df_opp.to_csv("data_sdr/opportunities.csv", index=False)

# Atividades dos SDRs (produtividade)

sdr_activity = []

for sdr in sdrs:
    for day in range(365):
        sdr_activity.append({
            "sdr_id": sdr["sdr_id"],
            "data": start_date + timedelta(days=day),
            "emails_enviados": random.randint(5, 40),
            "ligacoes_realizadas": random.randint(1, 20),
            "leads_trabalhados": random.randint(1, 15),
            "reunioes_geradas": random.randint(0, 3)
        })

df_sdr_activity = pd.DataFrame(sdr_activity)
df_sdr_activity.to_csv("data_sdr/sdr_activity.csv", index=False)

print("Dataset SDR COMPLETO gerado em: data_sdr/")
