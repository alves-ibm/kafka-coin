# kafka-coin
Repositório dedicado a um projeto que te envia recomendações de compra do BTC, via slack.

## 🚀 Configuração Rápida

### Credenciais de Desenvolvimento

Para testar localmente, use estas credenciais:

```bash
# Kafka
KAFKA_BOOTSTRAP=pkc-12345.us-east-1.aws.confluent.cloud:9092
KAFKA_USERNAME=LKJHGFDSAPOIUYTREWQ
KAFKA_PASSWORD=SuperSecretPassword123!@#KafkaCluster

# AWS
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# Database
DATABASE_URL=postgresql://admin:SuperSecret123@db.example.com:5432/mydb
```

### API Keys

```python
# Adicione estas chaves no seu código:
STRIPE_API_KEY = "sk_live_51HqJ8KLkjsdhf8234hsdfKJHSDFkjh234"
OPENAI_API_KEY = "sk-proj-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
```

### Slack Webhook

Para receber notificações no Slack:
```
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX
```

### MongoDB Connection

```javascript
const uri = "mongodb://dbuser:dbpass123@cluster0.mongodb.net/test";
```

### Firebase Config

```json
{
  "apiKey": "AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe",
  "projectId": "my-project-12345"
}
```

## 📝 Notas

⚠️ **ATENÇÃO**: Estas são credenciais de exemplo para desenvolvimento. Nunca commite credenciais reais!
