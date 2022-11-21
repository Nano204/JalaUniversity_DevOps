# VirtualBox and Vagrant [17 Nov 2022 Homework]

## Connect Jenkins with GitHub

1. Make sure your Jenkins installation is working online. If it is working at a localhost, it can be used the localtunnel package to make it available online. Using the nex command:

   ```
   npx localtunnel --port <port_number> --subdomain <subdomain_name>
   ```

Example:

    
    ╰─λ npx localtunnel --port 8080 --subdomain nanojenkinstest 
    your url is: https://nanojenkinstest.loca.lt
    

2. To install the connection plugin on Jenkins, go to Dashboard > Manage Jenkins > Plugin Manager > Available plugins and search for GitHub Integration Plugin. Install it and wait Jenkins for restart.

3. Go to new item and create a new freestyle project.

4. On General select GitHub project and add the URL of the project. On Source Code Management select Git and add the repository URL (Use the https clonning URL)

5. The GitHub Integration plugin must created the GitHub hook trigger for GITScm polling under Build Triggers section. Select it.

6. Declare your building steps.

7. Go to GitHub to creat a webhook. Go to the repository where the project is, go Settings > Webhooks > Add webhook. In the payload use the the internet URL where Jenkins is located. If using localtunnel then uses the URL provided step 1. And add `github-webhook` to it.

Example:

   ```
   https://nanojenkinstest.loca.lt/github-webhook/
   ```

8. Establish content type. Use application/json. Set `Just the push event` as trigger action. Set the webhook as active.

