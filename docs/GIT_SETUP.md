# Git & GitHub — setup and everyday use

A short, beginner-friendly guide for keeping this portfolio on GitHub.

## Git vs GitHub (in two sentences)

**Git** is the tool on your computer that tracks the history of your files — every
saved snapshot ("commit") is kept so you can see what changed and when. **GitHub** is
a website that stores a copy of that history online, so it's backed up and you can
share a link to it (for example, with universities).

## One-time setup on this computer

Tell git who you are (this stamps your name on every commit). These are already
filled in with your details — just run them once:

```bash
git config --global user.name "Kush Kumar"
git config --global user.email "k.kumar@ankvt.com"
```

> You already have a GitHub account (username **Websitemaxxer**), so there's nothing
> else to sign up for.

## Create the online repository (one time)

1. Go to https://github.com/new
2. **Repository name:** `robotics-portfolio`
3. **Do NOT** tick "Add a README", ".gitignore", or "license" — the repo must start
   **empty**, because this folder already has those files. (Adding them on GitHub
   creates a conflict that's annoying to untangle as a beginner.)
4. Leave it set to **Public** (see the note below), then click **Create repository**.

## Connect this folder and push it up (one time)

From inside this folder (`robotics-portfolio/`):

```bash
git init                 # start tracking this folder with git (skip if already done)
git add -A               # stage every file
git commit -m "Initial portfolio"   # save the first snapshot
git branch -M main       # name the branch "main"
git remote add origin https://github.com/Websitemaxxer/robotics-portfolio.git
git push -u origin main  # upload to GitHub
```

> If this portfolio was set up for you, the first commit and push may already be
> done — in that case you can skip straight to the **everyday habit loop** below.

## Signing in when you push (important)

When you `git push`, GitHub will ask you to authenticate. **GitHub no longer accepts
your account password here.** Use one of these:

- **Personal Access Token (easiest to start):** on GitHub go to
  **Settings → Developer settings → Personal access tokens → Tokens (classic) →
  Generate new token (classic)**, tick the **`repo`** scope, generate it, and **copy
  the token**. When git asks for your *password*, paste the **token** instead. (Save
  the token somewhere safe — GitHub only shows it once.)
- **SSH:** if you've already set up an SSH key with GitHub, use the SSH remote instead
  (`git@github.com:Websitemaxxer/robotics-portfolio.git`) and you won't be prompted
  for a token each time.

## Public or private?

This repo is **Public** on purpose: a public link is what you paste into a university
application or share with a teacher. There's nothing secret in a portfolio. If you
ever want to hide it, go to the repo's **Settings → General → Danger Zone → Change
visibility → Private** — you can flip it back to public anytime.

## Everyday habit loop

Each time you work on a project:

```bash
./scripts/new_entry.sh 01_arduino-starter-kit   # 1. add today's diary entry
# 2. open 01_planning/BUILD_DIARY.md and fill it in (be honest about failures!)
git add -A                                       # 3. stage your changes
git commit -m "Arduino: session on <what you did>"   # 4. save a snapshot
git push                                         # 5. upload to GitHub
```

That's the whole loop: **new entry → fill it in → add → commit → push.** Small, frequent
commits are better than one giant one — they show steady, dated progress.

## Starting a new project later

```bash
./scripts/new_project.sh 02_line-follower "Line Follower Robot"
```

This copies the template into `projects/02_line-follower/`, fills in the project name,
and prints the next steps. Then add a row to the top-level `README.md` and start its
build diary with `new_entry.sh`.

## A note on large files

GitHub is built for text (code, notes), not big media, and it rejects single files
over 100 MB.

- **Videos:** keep demo clips short, or upload them to **YouTube/Google Drive** and put
  the link in the project README instead of committing the video file.
- **CAD:** heavy CAD files (`.stl`, `.step`, `.zip`) are ignored by `.gitignore` by
  default. When a project genuinely needs to version them, set up **Git LFS** (Large
  File Storage) — see the comments at the bottom of `.gitignore` for the exact commands.
