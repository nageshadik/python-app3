# python-platform-app





# helm install python-app -n python . --create-namespace



# helm uninstall python-app -n python



# helm upgrade --install argocd argo/argo-cd  -n argocd --create-namespace -f values-argo.yml


cat <<EOF | kubectl apply -n actions-runner-system -f -
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: python-app
spec:
  replicas: 1
  template:
    spec:
      repository: adi-nagesh/python-platform-app
EOF




        #  ARGOCD_VERSION=$(curl --silent "https://api.github.com/repos/argoproj/argo-cd/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/')
        #  curl -sSL -o /tmp/argocd-${ARGOCD_VERSION} https://github.com/argoproj/argo-cd/releases/download/${ARGOCD_VERSION}/argocd-linux-amd64
        #  chmod +x /tmp/argocd-${VERSION}
        #  sudo mv /tmp/argocd-${VERSION} /usr/local/bin/argocd 
        #  argocd version --client


##backstage
1 download node docker image 
docker pull node:18-bookworm-slim

 mkdir backstage-app


 docker run --rm -p 3000:3000 -p 7007:7007 -ti -v /Users/nagesh/Desktop/platform/backstage-app:/app -w /app node:18-bookworm-slim bash


 apt udate 
 apt-get install python3
 apt install -y build-essential

 npx @backstage/create-app@latest

 yarn start 



 # configure host to listen on 0.0.0.0.

 app:
  title: Scaffolded Backstage App
  baseUrl: http://localhost:3000
  listen:
    host: 0.0.0.0

# configure auth to backstage using github

  you must create either a GitHub App or an OAuth App from the GitHub developer settings. 


  modify app-config.local.yml


  app:
  listen:
    host: 0.0.0.0

auth:
  environment: development
  providers:
    github:
      development:
        clientId: ${AUTH_GITHUB_CLIENT_ID}
        clientSecret: ${AUTH_GITHUB_CLIENT_SECRET}
        ## uncomment if using GitHub Enterprise
        # enterpriseInstanceUrl: ${AUTH_GITHUB_ENTERPRISE_INSTANCE_URL}
        ## uncomment to set lifespan of user session
        # sessionDuration: { hours: 24 } # supports `ms` library format (e.g. '24h', '2 days'), ISO duration, "human duration" as used in code
        signIn:
          resolvers:
            # See https://backstage.io/docs/auth/github/provider#resolvers for more resolvers
            - resolver: usernameMatchingUserEntityName

# provide env variables in docker run command 


 docker run --rm -e AUTH_GITHUB_CLIENT_ID=Ov23liaOEcz08gLAcy1c -e AUTH_GITHUB_CLIENT_SECRET=<   > -p 3000:3000  -p 7007:7007 -ti -v /Users/nagesh/Desktop/platform/backstage-app:/app -w /app node:18-bookworm-slim bash


# backend installation 

yarn --cwd packages/backend add @backstage/plugin-auth-backend-module-github-provider


in packages/backend/src/index.ts


# software templates 















