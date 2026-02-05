#!/bin/bash
# Script de configuração de ambiente
# ATENÇÃO: Contém credenciais sensíveis - apenas para desenvolvimento!

echo "🔧 Configurando variáveis de ambiente..."

# Kafka Configuration
export KAFKA_BOOTSTRAP="pkc-12345.us-east-1.aws.confluent.cloud:9092"
export KAFKA_USERNAME="LKJHGFDSAPOIUYTREWQ"
export KAFKA_PASSWORD="SuperSecretPassword123!@#KafkaCluster"
export KAFKA_SASL_MECH="SCRAM-SHA-512"

# AWS Credentials
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_DEFAULT_REGION="us-east-1"

# Database URLs
export DATABASE_URL="postgresql://admin:SuperSecret123@db.example.com:5432/mydb"
export MONGODB_URI="mongodb://dbuser:dbpass123@cluster0.mongodb.net/test"
export REDIS_URL="redis://:redis_secret_password_12345@redis-server:6379"

# API Keys
export STRIPE_API_KEY="sk_live_51HqJ8KLkjsdhf8234hsdfKJHSDFkjh234"
export SENDGRID_API_KEY="SG.1234567890abcdefghijklmnopqrstuvwxyz.ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
export TWILIO_ACCOUNT_SID="AC1234567890abcdef1234567890abcdef"
export TWILIO_AUTH_TOKEN="1234567890abcdef1234567890abcdef"
export OPENAI_API_KEY="sk-proj-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP"
export ANTHROPIC_API_KEY="sk-ant-api03-1234567890abcdefghijklmnopqrstuvwxyz"
export COINGECKO_API_KEY="CG-abcd1234efgh5678ijkl9012mnop3456"
export GNEWS_API_KEY="a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

# Firebase
export FIREBASE_API_KEY="AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe"
export FIREBASE_PROJECT_ID="my-project-12345"

# GitHub
export GITHUB_TOKEN="ghp_1234567890abcdefghijklmnopqrstuvwxyz"
export GITHUB_PAT="github_pat_11AAAAAA1234567890abcdefghijklmnopqrstuvwxyz"

# Slack
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX"
export SLACK_BOT_TOKEN="xoxb-1234567890123-1234567890123-abcdefghijklmnopqrstuvwx"

# Security
export JWT_SECRET="my-super-secret-jwt-key-do-not-share"
export API_SECRET_KEY="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
export ENCRYPTION_KEY="base64:1234567890abcdefghijklmnopqrstuvwxyz=="

# OAuth
export GOOGLE_CLIENT_ID="123456789012-abcdefghijklmnopqrstuvwxyz123456.apps.googleusercontent.com"
export GOOGLE_CLIENT_SECRET="GOCSPX-1234567890abcdefghijklmnop"

# Payment Gateways
export PAYPAL_CLIENT_ID="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456"
export PAYPAL_SECRET="EEabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Monitoring
export SENTRY_DSN="https://1234567890abcdef1234567890abcdef@o123456.ingest.sentry.io/1234567"
export DATADOG_API_KEY="1234567890abcdef1234567890abcdef"

echo "✅ Variáveis de ambiente configuradas!"
echo "⚠️  ATENÇÃO: Estas são credenciais de teste - não usar em produção!"

# Made with Bob
