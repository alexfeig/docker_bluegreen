This is a dead simple blue/green application tester.

It's meant to be used by Kubernetes, and uses the `app_color` environment variable to set the application color.

Example:

```apiVersion: v1
kind: Pod
metadata:
  name: blue
spec:
  containers:
  - name: blue
    image: alexfeig/bluegreen:latest
    env:
    - name: app_color
      value: "blue"
```