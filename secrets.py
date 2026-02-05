"""
Arquivo de secrets para desenvolvimento
ATENÇÃO: NÃO COMMITAR EM PRODUÇÃO!
"""

# ==================== KAFKA ====================
KAFKA_CONFIG = {
    "bootstrap_servers": "pkc-12345.us-east-1.aws.confluent.cloud:9092",
    "username": "LKJHGFDSAPOIUYTREWQ",
    "password": "SuperSecretPassword123!@#KafkaCluster",
    "sasl_mechanism": "SCRAM-SHA-512"
}

# ==================== AWS ====================
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"
AWS_S3_BUCKET = "my-crypto-bucket"

# ==================== DATABASES ====================
POSTGRES_HOST = "db.example.com"
POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "SuperSecret123"
POSTGRES_DB = "mydb"
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

MONGODB_USERNAME = "dbuser"
MONGODB_PASSWORD = "dbpass123"
MONGODB_URI = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.mongodb.net/test"

REDIS_PASSWORD = "redis_secret_password_12345"
REDIS_URL = f"redis://:{REDIS_PASSWORD}@redis-server:6379"

# ==================== API KEYS ====================
STRIPE_API_KEY = "sk_live_51HqJ8KLkjsdhf8234hsdfKJHSDFkjh234"
STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
STRIPE_WEBHOOK_SECRET = "whsec_1234567890abcdefghijklmnopqrstuvwxyz"

SENDGRID_API_KEY = "SG.1234567890abcdefghijklmnopqrstuvwxyz.ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
SENDGRID_FROM_EMAIL = "noreply@example.com"

TWILIO_ACCOUNT_SID = "AC1234567890abcdef1234567890abcdef"
TWILIO_AUTH_TOKEN = "1234567890abcdef1234567890abcdef"
TWILIO_PHONE_NUMBER = "+15551234567"

# ==================== AI SERVICES ====================
OPENAI_API_KEY = "sk-proj-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP"
OPENAI_ORG_ID = "org-1234567890abcdefghijklmnop"

ANTHROPIC_API_KEY = "sk-ant-api03-1234567890abcdefghijklmnopqrstuvwxyz"

COHERE_API_KEY = "1234567890abcdefghijklmnopqrstuvwxyz"

HUGGINGFACE_TOKEN = "hf_1234567890abcdefghijklmnopqrstuvwxyz"

# ==================== NEWS & DATA APIs ====================
COINGECKO_API_KEY = "CG-abcd1234efgh5678ijkl9012mnop3456"
GNEWS_API_KEY = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
NEWSAPI_KEY = "1234567890abcdef1234567890abcdef"
ALPHA_VANTAGE_KEY = "ABCDEFGHIJKLMNOP"

# ==================== FIREBASE ====================
FIREBASE_API_KEY = "AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe"
FIREBASE_PROJECT_ID = "my-project-12345"
FIREBASE_AUTH_DOMAIN = "my-project-12345.firebaseapp.com"
FIREBASE_STORAGE_BUCKET = "my-project-12345.appspot.com"
FIREBASE_MESSAGING_SENDER_ID = "123456789012"
FIREBASE_APP_ID = "1:123456789012:web:abcdef1234567890"

# ==================== GITHUB ====================
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
GITHUB_PERSONAL_ACCESS_TOKEN = "github_pat_11AAAAAA1234567890abcdefghijklmnopqrstuvwxyz"
GITHUB_WEBHOOK_SECRET = "github_webhook_secret_1234567890"

# ==================== SLACK ====================
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX"
SLACK_BOT_TOKEN = "xoxb-1234567890123-1234567890123-abcdefghijklmnopqrstuvwx"
SLACK_APP_TOKEN = "xapp-1-A01234567-1234567890123-abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz"
SLACK_SIGNING_SECRET = "1234567890abcdef1234567890abcdef"

# ==================== SECURITY ====================
JWT_SECRET = "my-super-secret-jwt-key-do-not-share"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION = 3600

API_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
ENCRYPTION_KEY = "base64:1234567890abcdefghijklmnopqrstuvwxyz=="

SESSION_SECRET = "session-secret-key-1234567890abcdef"
COOKIE_SECRET = "cookie-secret-key-abcdef1234567890"

# ==================== OAUTH ====================
GOOGLE_CLIENT_ID = "123456789012-abcdefghijklmnopqrstuvwxyz123456.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "GOCSPX-1234567890abcdefghijklmnop"

FACEBOOK_APP_ID = "1234567890123456"
FACEBOOK_APP_SECRET = "1234567890abcdef1234567890abcdef"

TWITTER_API_KEY = "abcdefghijklmnopqrstuvwxy"
TWITTER_API_SECRET = "1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdef"
TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAA1234567890abcdefghijklmnopqrstuvwxyz"

# ==================== PAYMENT GATEWAYS ====================
PAYPAL_CLIENT_ID = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456"
PAYPAL_SECRET = "EEabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

MERCADOPAGO_ACCESS_TOKEN = "APP_USR-1234567890123456-123456-1234567890abcdef1234567890abcdef-123456789"
MERCADOPAGO_PUBLIC_KEY = "APP_USR-1234567890abcdef-123456-1234567890abcdef-123456789-1234567890"

# ==================== ANALYTICS ====================
GOOGLE_ANALYTICS_ID = "G-ABCDEFGHIJ"
MIXPANEL_TOKEN = "1234567890abcdef1234567890abcdef"
SEGMENT_WRITE_KEY = "1234567890abcdefghijklmnopqrstuvwxyz"

# ==================== MONITORING ====================
SENTRY_DSN = "https://1234567890abcdef1234567890abcdef@o123456.ingest.sentry.io/1234567"
DATADOG_API_KEY = "1234567890abcdef1234567890abcdef"
NEW_RELIC_LICENSE_KEY = "1234567890abcdef1234567890abcdef12345678"

# ==================== EMAIL ====================
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "noreply@example.com"
SMTP_PASSWORD = "smtp_password_123456"

MAILGUN_API_KEY = "key-1234567890abcdef1234567890abcdef"
MAILGUN_DOMAIN = "mg.example.com"

# ==================== DOCKER & REGISTRY ====================
DOCKER_HUB_USERNAME = "myusername"
DOCKER_HUB_PASSWORD = "dckr_pat_1234567890abcdefghijklmnopqrstuvwxyz"

GITHUB_CONTAINER_REGISTRY_TOKEN = "ghcr_1234567890abcdefghijklmnopqrstuvwxyz"

# ==================== CI/CD ====================
CIRCLECI_TOKEN = "1234567890abcdef1234567890abcdef1234567890"
TRAVIS_TOKEN = "abcdefghijklmnopqrstuvwxyz"
JENKINS_API_TOKEN = "1234567890abcdef1234567890abcdef12"

# ==================== MISC ====================
RECAPTCHA_SITE_KEY = "6LcAbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
RECAPTCHA_SECRET_KEY = "6LcAbCdEfGhIjKlMnOpQrStUvWxYz1234567890"

CLOUDFLARE_API_TOKEN = "1234567890abcdefghijklmnopqrstuvwxyz"
CLOUDFLARE_ZONE_ID = "1234567890abcdef1234567890abcdef"

# ==================== PRIVATE KEYS ====================
RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
OPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR
-----END RSA PRIVATE KEY-----"""

SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEA1234567890abcdefghijklmnopqrstuvwxyz
-----END OPENSSH PRIVATE KEY-----"""

if __name__ == "__main__":
    print("⚠️  ATENÇÃO: Este arquivo contém credenciais sensíveis!")
    print("🔒 Nunca commite este arquivo em repositórios públicos!")

# Made with Bob
