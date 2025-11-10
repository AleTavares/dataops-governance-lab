import logging

def alerta_qualidade(dataset, problema, severidade):
    logging.warning(f"[{severidade}] {dataset}: {problema}")
    if severidade == "Crítico":
        print("🔔 Notificação enviada ao Data Owner")
    elif severidade == "Médio":
        print("🔔 Notificação enviada ao Data Steward")