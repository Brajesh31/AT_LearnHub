# 🐧 Linux learning path

## Goal
Practice command-line navigation, file inspection, filesystem concepts, and simple shell scripts.

## Suggested sequence
1. Read the Linux file-system reference material.
2. Review the command notes in the `Linux/` directory.
3. Practice navigation, listing, searching, copying, moving, and permissions in a disposable directory.
4. Read `Linux/myscript.sh` before running it.
5. Inspect archives with `tar -tf archive.tar` before extracting.

## Safe practice commands
```bash
pwd
ls -lah
mkdir -p ~/learnhub-lab
cd ~/learnhub-lab
touch sample.txt
printf 'learning\n' > sample.txt
cat sample.txt
```

## Safety
Do not experiment with `sudo`, recursive deletion, disk formatting, system configuration, or ownership changes on a machine containing important data. Review shell quoting and redirection before execution.
