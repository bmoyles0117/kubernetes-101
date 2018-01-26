# Kubernetes 101

This content is intended for a Kubernetes 101 course which includes a few
sample applications that work together to demonstrate Kubernetes concepts.

## Run in a Kubernetes cluster

Configure kubectl to be configured to the target cluster and run:

`kubectl apply -f ./k8s/`

## Build docker images

All of the applications in this repository are able to be built using the
command below from the relevant subdirectory:

`docker build -t {desired-tag} .`

After you build your tagged image, you can push it to whatever docker registry
you'd like, update the relevant k8s yaml file, and apply it to your cluster.