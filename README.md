## Implement SAST + DAST through Github actions

The repository is supposed to implement SAST+DAST checks using github actions against a vulnerable python application which allows RCE. Goal is to detect it before it gets pushed into production.

### Roadmap

-   [x] Python vulnerable RCE application
-   [ ] Github actions
    -   [ ] Implement SAST using bandit
    -   [ ] Implement DAST using OWASP ZAP (need app deployed somewhere - k8s to the rescue!)
    -   [ ] Deploy application using Kubernetes
-   [ ] Post gist of found vulnerabilities in Slack
    -   [ ] Use hashicorp vault to reference slack bot credentials
