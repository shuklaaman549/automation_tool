Automatic LeetCode Submission
This project automates the daily submission of LeetCode problems using GitHub Actions and Selenium. The submissions are scheduled using cron syntax, making it easy to manage and automate your LeetCode streak.

Introduction
This repository hosts a script that automates the process of solving and submitting a LeetCode problem daily. The automation is set up using GitHub Actions and Selenium. The submission is triggered daily by a scheduled cron job, ensuring that you maintain your streak and practice regularly.

How to Set It Up
Clone the Repository: Start by cloning this repository to your local machine.

bash
Copy code
git clone https://github.com/your-username/automatic_submission.git
Set Up GitHub Secrets: You'll need to store your LeetCode credentials as secrets in your GitHub repository.

Go to your repository on GitHub.
Click on Settings.
Navigate to Secrets and variables > Actions.
Add the following secrets:
LEETCODE_USERNAME: Your LeetCode username.
LEETCODE_PASSWORD: Your LeetCode password.
Update the Cron Schedule: The script is currently scheduled to run daily at 9:00 PM IST (3:30 PM UTC). You can modify the cron schedule in the .github/workflows/leetcode_submission.yml file if needed.

Run the Workflow: Once everything is set up, the workflow will automatically run daily at the scheduled time. You can also trigger it manually from the GitHub Actions tab.

Word of Caution
Security: Ensure that your LeetCode credentials are securely stored in GitHub Secrets. Never hardcode your credentials in the code.
LeetCode Terms of Service: Be aware of LeetCode's terms and conditions regarding automated submissions. Use this script responsibly.
