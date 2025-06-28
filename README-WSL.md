# Install WSL

## Install UV
```cmd
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
    uv 0.7.15
uvx --version
    uvx 0.7.15
```

## Git clone the repo and setup
```cmd
mkdir projects
cd projects
git clone https://www.github.com/christseng89/agents-ai.git

uv sync
nano .env
# Add your .env variables here, or copy from .env_sample    
```

## GitHub SSH Setup
```cmd
ssh-keygen -t ed25519 -C "samfire5200@gmail.com"
cat ~/.ssh/id_ed25519.pub
```

### 📝 Add Your SSH Key to GitHub
- Go to GitHub → Settings → SSH and GPG keys
    - Click New SSH key
    - Title: e.g. WSL Key
    - Paste your public key
    - Click Add SSH key

- ✅ Done!

### Test SSH Connection
```cmd
ssh -T git@github.com
    Hi christseng89! You've successfully authenticated, but GitHub does not provide shell access

git remote -v
    origin  https://www.github.com/christseng89/agents-ai.git (fetch)
    origin  https://www.github.com/christseng89/agents-ai.git (push)
git remote set-url origin git@github.com:christseng89/agents-ai.git

git remote -v
    origin  git@github.com:christseng89/your-repo.git (fetch)
    origin  git@github.com:christseng89/your-repo.git (push)

git add .
git commit -m "Your commit message"
git push     
```