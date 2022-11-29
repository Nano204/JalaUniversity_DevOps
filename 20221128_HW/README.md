# Terraform [28 Nov 2022 Homework]

## First Terraform project on Arch

1. Install terraform using:

```
╰─λ sudo pacman terraform
```

2. Install terraform/HashiCorp extension on VScode (optional step).
3. Go to [Providers page](https://registry.terraform.io/browse/providers) to select a provider. In this case wee will use [Docker](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs)
4. Go to providers's documentation and compy the `Example of usage` in a new `main.tf` file.
5. Make some changes on `main.tf`. For example, if using the exact code find on `Example of usage`, iis possible to find this error:

```js
Error: container exited immediately
```

So to keepo the container running the `resource` should be like following:

```terraform
# Create a container
resource "docker_container" "server-container" {
  image             = docker_image.ubuntu.image_id
  name              = "terraform-docker-test"
  must_run          = true
  publish_all_ports = true
  command = [
    "sleep",
    "30"
  ]
}
```

This will help to keep container running for 30 seconds and will help to test if Terraform configuration is working.

6. Initialize Terraform in the folder where `main.tf` is located.

```
terraform init
```

7. Then test in dry what Terraform would do.\

```
terraform plan
```

8. Run Terraform

```
terraform apply
```
