# Automatic LeetCode Submission

This project automates the daily submission of LeetCode problems using GitHub Actions and Selenium. The submissions are scheduled using cron syntax, making it easy to manage and automate your LeetCode streak.

## Introduction

This repository hosts a script that automates the process of solving and submitting a LeetCode problem daily. The automation is set up using GitHub Actions and Selenium. The submission is triggered daily by a scheduled cron job, ensuring that you maintain your streak and practice regularly. Also the chrome is run in headless mode and wait times have been reduced at their is 1min limit for github actions in free tier.

## How to Set It Up

### 1. Clone the Repository

Start by cloning this repository to your local machine.

```bash
git clone https://github.com/your-username/automatic_submission.git
```

### 2. Set Up GitHub Secrets

You'll need to store your LeetCode credentials as secrets in your GitHub repository.

1. Go to your repository on GitHub.
2. Click on "Settings".
3. Navigate to "Secrets and variables" > "Actions".
4. Add the following secrets:
   - `LEETCODE_USERNAME`: Your LeetCode username.
   - `LEETCODE_PASSWORD`: Your LeetCode password.

## 2.1 Alternate Way (Not Recommended)
- If you are lazy i don't want soo much hasle just replace the credentials locally and make the repo *private*
```
# Log in (replace 'username' and 'password' with your credentials)
username = "<username>"
password = "<password>"
```

### 3. Update the Cron Schedule

The script is currently scheduled to run daily at 9:00 PM IST (3:30 PM UTC). You can modify the cron schedule in the `.github/workflows/leetcode_submission.yml` file if needed.

### 4. Run the Workflow

Once everything is set up, the workflow will automatically run daily at the scheduled time. You can also trigger it manually from the GitHub Actions tab.

## Word of Caution

- **Security**: Ensure that your LeetCode credentials are securely stored in GitHub Secrets. Never hardcode your credentials in the code.
- **LeetCode Terms of Service**: Be aware of LeetCode's terms and conditions regarding automated submissions. Use this script responsibly.

## Personal take
- I don't support use of these type tools but i know it hurts real bad when you sleep early by mistake 😅 and break your looong streak.