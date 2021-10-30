'''
Parse bandit results and only return HIGH/MEDIUM results
'''

from slack_sdk import WebClient, errors
import json
import os


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip()

def parse_bandit_output(contents):
    message = ''
    json_data = json.loads(contents)

    metrics = json_data.get('metrics').get('_totals')
    results = json_data.get('results')
    total_issues = len(results)

    if total_issues != 0:

        message += f"*Total issues found:* {total_issues}\n\n"
        message += f":red_circle: *High severity:* {int(metrics.get('SEVERITY.HIGH'))}\n"
        message += f":large_blue_circle: *Medium severity:* {int(metrics.get('SEVERITY.MEDIUM'))}\n"
        message += f":white_circle: *Low severity:* {int(metrics.get('SEVERITY.LOW'))}\n\n"

        for issues in results:
            code = issues.get('code')
            filename = issues.get('filename')
            issue_severity = issues.get('issue_severity')
            issue_text = issues.get('issue_text')
            line_number = issues.get('line_number')
            more_info = issues.get('more_info')

            message += (f"*Title:* {issue_text}\n")
            message += (f"*Severity:* `{issue_severity}`\n")
            message += (f"*File name:* {filename}\n")
            message += (f"*Line Number:* {line_number}\n")
            message += (f"*Vulnerable code:*\n```{code}```\n")
            message += (f"*More on the issue:* {more_info}\n\n\n")

        print(message)
        post_to_slack(message)
        
    else:
        print("[#] Bandit found no issues :D")

def post_to_slack(message):
    slack_token = os.environ.get("SLACK_BOT_TOKEN")
    client = WebClient(token=slack_token)

    channel_id = os.environ.get("SLACK_CHANNEL_ID")
    client.chat_postMessage(channel=channel_id, text=message)

def main():
    bandit_output_file = 'bandit-output.json'
    file_contents = read_file(bandit_output_file)
    parse_bandit_output(file_contents)

if __name__ == '__main__':
    main()