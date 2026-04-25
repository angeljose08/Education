# 🚀 Google Cloud Run Deployment Guide

## Architecture
```
GitHub Repository → Cloud Build → Container Registry → Cloud Run → Public URL
```

---

## Prerequisites

### 1. **Google Cloud Account Setup**
```bash
# Create a Google Cloud project
# Go to: https://console.cloud.google.com/
# Note: You need billing enabled

# Install Google Cloud SDK
# On macOS: brew install google-cloud-sdk
# On Windows: Download from https://cloud.google.com/sdk/docs/install
# On Linux: curl https://sdk.cloud.google.com | bash
```

### 2. **Authenticate with Google Cloud**
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

---

## Deployment Methods

### **Method 1: Deploy via Cloud Console (Easiest)**

1. Go to **Google Cloud Console**: https://console.cloud.google.com/
2. Navigate to **Cloud Run**
3. Click **CREATE SERVICE**
4. Choose **Deploy one revision from an image**
5. Click **Deploy**
6. Fill in:
   - **Service name**: `election-education`
   - **Region**: `us-central1` (or closest to you)
   - **Authentication**: Check "Allow unauthenticated invocations"

7. Click **DEPLOY** and wait (3-5 minutes)

**Your Cloud Run URL will appear**: `https://election-education-xxxxx.run.app`

---

### **Method 2: Deploy via GitHub Integration**

#### Step 1: Connect GitHub Repository
```bash
# In Cloud Console:
1. Go to Cloud Build → Triggers
2. Click CREATE TRIGGER
3. Connect GitHub repository
4. Authorize Cloud Build
5. Select angeljose08/Education
```

#### Step 2: Configure Build Configuration
```
Build Type: Cloud Run
Trigger name: education-deploy
Branch: ^main$
Build location: Cloud Build
Build configuration: cloudbuild.yaml
Service account: [default]
```

#### Step 3: Deploy Automatically
```bash
# Every push to main branch will automatically:
# 1. Build Docker image
# 2. Push to Container Registry
# 3. Deploy to Cloud Run
# 4. Generate public URL
```

---

### **Method 3: Deploy via Command Line (Most Control)**

#### Step 1: Install Required Tools
```bash
# Install gcloud SDK (if not installed)
curl https://sdk.cloud.google.com | bash

# Initialize
gcloud init
```

#### Step 2: Set Environment Variables
```bash
export PROJECT_ID="your-project-id"
export REGION="us-central1"
export SERVICE_NAME="election-education"
```

#### Step 3: Build & Deploy
```bash
# Option A: Direct deployment (recommended)
gcloud run deploy $SERVICE_NAME \
  --source . \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars=DEBUG=False,ENVIRONMENT=production

# Option B: Build image first, then deploy
# Build image
gcloud builds submit \
  --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

# Deploy image
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated
```

---

## Getting Your Cloud Run URL

### **From Cloud Console:**
1. Go to **Cloud Run**
2. Click your service name (`election-education`)
3. Copy the **Service URL** (at the top of the details page)

Format: `https://election-education-xxxxx.run.app`

### **From Command Line:**
```bash
gcloud run services describe election-education \
  --platform managed \
  --region us-central1 \
  --format='value(status.address.url)'
```

Output:
```
https://election-education-xxxxx.run.app
```

---

## Environment Variables for Production

Create a `.env.production` file with:
```env
DEBUG=False
SECRET_KEY=your-secure-random-key
ENVIRONMENT=production
ALLOWED_HOSTS=election-education-xxxxx.run.app
DATABASE_URL=postgresql://user:password@cloud-sql-instance
```

Set in Cloud Run:
```bash
gcloud run services update election-education \
  --update-env-vars=DEBUG=False,ENVIRONMENT=production
```

---

## Database Setup for Production

### Use Google Cloud SQL (PostgreSQL)

#### Create Cloud SQL Instance:
```bash
gcloud sql instances create education-db \
  --database-version=POSTGRES_15 \
  --region=$REGION \
  --tier=db-f1-micro
```

#### Create Database:
```bash
gcloud sql databases create education \
  --instance=education-db
```

#### Create User:
```bash
gcloud sql users create django \
  --instance=education-db \
  --password=SECURE_PASSWORD
```

#### Update Settings:
```python
# In settings.py, update for Cloud SQL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'education',
        'USER': 'django',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '/cloudsql/PROJECT_ID:REGION:INSTANCE_NAME',
    }
}
```

---

## Custom Domain (Optional)

### Map Your Own Domain:
```bash
gcloud run services update election-education \
  --region $REGION \
  --update-labels=domain=yourdomain.com

# Then add DNS record:
# CNAME yourdomain.com → election-education-xxxxx.run.app
```

---

## Monitoring & Logs

### View Deployment Logs:
```bash
gcloud run services describe election-education --region $REGION
```

### Stream Real-time Logs:
```bash
gcloud run services logs read election-education --region $REGION --limit 50 --follow
```

### View in Console:
```
https://console.cloud.google.com/run/detail/[REGION]/election-education/logs
```

---

## Cost Estimation

**Cloud Run Pricing (as of 2024):**
- **Compute**: $0.00002400 per vCPU-second
- **Memory**: $0.0000025 per GB-second
- **Requests**: $0.40 per million requests
- **Free tier**: 2M requests/month + 360K vCPU-seconds

For a small project: **$5-15/month**

---

## Troubleshooting

### Issue: "Permission denied" error
```bash
# Grant Cloud Run admin role to your user
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member=user:your-email@gmail.com \
  --role=roles/run.admin
```

### Issue: Static files not loading
```bash
# Run migrations and collect static files
gcloud run services update election-education \
  --set-env-vars=STATIC_ROOT=/tmp/static
```

### Issue: 502 Bad Gateway
```bash
# Check logs for errors
gcloud run services logs read election-education --limit 50

# Verify Docker image runs locally
docker run -p 8080:8080 gcr.io/$PROJECT_ID/election-education
```

---

## Quick Summary

| Method | Ease | Control | Time |
|--------|------|---------|------|
| Cloud Console | ⭐⭐⭐⭐⭐ | ⭐ | 3 min |
| GitHub Integration | ⭐⭐⭐⭐ | ⭐⭐⭐ | 5 min |
| CLI Deploy | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 5 min |

---

## Your Deployed Application

After deployment, you can access:

- **Home**: `https://election-education-xxxxx.run.app`
- **Admin**: `https://election-education-xxxxx.run.app/admin`
- **API**: `https://election-education-xxxxx.run.app/api`

---

**Need help?** Check [Cloud Run Documentation](https://cloud.google.com/run/docs)
