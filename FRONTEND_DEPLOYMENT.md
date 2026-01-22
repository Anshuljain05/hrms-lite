# Frontend Deployment to Vercel (Free Tier)

## Quick Deploy Steps

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Navigate to frontend:**
   ```bash
   cd frontend
   ```

3. **Deploy:**
   ```bash
   vercel
   ```
   - Choose "Y" for account linking if first time
   - Select your GitHub project
   - Accept defaults (should auto-detect Vite settings)

4. **Set Environment Variables in Vercel Dashboard:**
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Select your project → Settings → Environment Variables
   - Add:
     ```
     VITE_API_URL = https://your-railway-backend-url.up.railway.app/api
     ```
   - Redeploy (or push to trigger auto-deploy)

## Alternative: Deploy via GitHub (Recommended - Auto-redeploy)

1. **Push to GitHub** (if not already)
   ```bash
   git add .
   git commit -m "Fix frontend API calls + add Vercel config"
   git push
   ```

2. **Connect to Vercel:**
   - Go to [vercel.com/new](https://vercel.com/new)
   - Import your GitHub repo
   - Select `frontend` folder as root
   - Add Environment Variable:
     ```
     VITE_API_URL = https://your-railway-backend-url.up.railway.app/api
     ```
   - Deploy!

## Environment Variables Reference

- **Local dev:** `http://localhost:8000/api`
- **Production:** `https://your-backend.railway.app/api`

Get your Railway backend URL from Railway dashboard → your-app → Share → Public URL

## Files Changed

✅ Fixed `employee_id` / `full_name` (snake_case) in:
- `Employees.jsx`
- `Attendance.jsx`

✅ Added:
- `vercel.json` - Deployment config
- `.env.example` - Environment reference

Deploy and share the Vercel URL! 🚀
