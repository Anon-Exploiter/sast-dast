## Implement SAST + DAST through Github actions

The repository is supposed to implement SAST+DAST checks using github actions against a vulnerable python application which allows RCE. Goal is to detect it before it gets pushed into production.

### Roadmap

-   [x] Python vulnerable RCE application
-   [ ] Github actions (executes on PR to main/master branch)
    -   [x] Implement SAST using bandit and post results in slack
    -   [ ] Implement DAST using OWASP ZAP (need app deployed somewhere - k8s to the rescue!)
    -   [ ] Deploy application using Kubernetes for OWASP ZAP scan
-   [x] Post gist of found vulnerabilities in Slack
    -   [x] SAST - Use hashicorp vault to reference slack bot credentials
    -   [ ] DAST - Use hashicorp vault to reference slack bot credentials
