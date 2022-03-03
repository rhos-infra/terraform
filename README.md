# Terraform

## General

Infrared plugin to provision infrastructure as code using [terraform](https://www.terraform.io).

## Requirements

**User must ensure that all required authentication methods are present and exposed to terraform,
this is not covered by this playbook**.

NOTE: This list below was tested, previous releases might be supported.

* `ansible >= 2.9`.
* [infrared](https://github.com/redhat-opnestack/infrared) (optional).

## Installation:

If using as Ansible playbooks:  
Clone this repository:
```bash
git clone https://github.com/rhos-infra/terraform
```
Install required Ansible galaxy collections:
```bash
ansble-galaxy collection install -r requirements.yaml
```

If using infrared:
```bash
infrared plugin add https://github.com/rhos-infra/terraform
```

## Inventory
The play does not require an inventory and by default will run from `localhost`.  
If required it can be configured to run from remote host.  
Please ensure that a proper inventory is present and used (for infrared refer to `infrared terraform --help`)
and `hosts_pattern` is supplied.

## Parameters

| Ansible Variable                 | Infrared CLI Argument              | Description                                                                       | Default | Ansible Example                                                                   | Infrared Example                                                                                         |
|----------------------------------|------------------------------------|-----------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `hosts_pattern`                  | `--hosts-pattern`                  | Ansible hosts string. **Required**                                                | `null`  | `undercloud`                                                                      | `--hosts-pattern="undercloud"`                                                                           |
| `binary_archive_url`             | `--binary-archive-url`             | URL to terraform binary archive. **Required**                                     | `null`  | `https://releases.hashicorp.com/terraform/1.1.5/terraform_1.1.5_darwin_arm64.zip` | `--binary-archive-url='https://releases.hashicorp.com/terraform/1.1.5/terraform_1.1.5_darwin_arm64.zip'` |
| `binary_archive_sha256_checksum` | `--binary-archive-sha256-checksum` | SHA256 checksum of terraform binary archive. **Required**                         | `null`  | `723363af9524c0897e9a7d871d27f0d96f6aafd11990df7e6348f5b45d2dbe2c.`               | `--binary-archive-sha256-checksum='723363af9524c0897e9a7d871d27f0d96f6aafd11990df7e6348f5b45d2dbe2c.'`   |
| `terraform_plan_state`          | `--state`                          | Terraform infrastructure state. **Required** **Choices:** `['present', 'absent']` | `null`  | `null`                                                                            | `--state='present'`                                                                                      |
| `terraform_check_mode`           | `--project-path`                   | Checks terraform plan.                                                            | `False` | `True`                                                                            | `--check-mode`                                                                                           |
| `terraform_project_path`         | `--project-path`                   | Path to terraform project containing  `main.tf`. **Required**                     | `null`  | `/path/to/project`                                                                | `--project-path='/path/to/project'`                                                                      |

## Usage

If using `infrared`, user supplied arguments (`-e`) override `infrared` provided
values.

Working with variables files (`-e @/path/to/file.yaml`) is more convenient.

### Ansible Examples

Execute terraform plan from macOS local host:

```bash
ansible-playbook -vvvv main.yaml -e binary_archive_url='https://releases.hashicorp.com/terraform/1.1.5/terraform_1.1.5_darwin_arm64.zip' -e binary_archive_sha256_checksum='723363af9524c0897e9a7d871d27f0d96f6aafd11990df7e6348f5b45d2dbe2c.' -e terraform_plan_state='present' -e terraform_check_mode='False' -e terraform_project_path='/tmp/'
```

### Infrared Examples

Execute terraform plan from linux local host:

```bash
infrared terraform -vvvv --binary-archive-url='https://releases.hashicorp.com/terraform/1.1.5/terraform_1.1.5_linux_arm64.zip' --binary-archive-sha256-checksum='2fb6324c24c14523ae63cedcbc94a8e6c1c317987eced0abfca2f6218d217ca5' --state present --project-path '/tmp/'
```
