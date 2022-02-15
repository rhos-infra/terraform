---

plugin_type: provision
entry_point: main.yaml
subparsers:
    terraform:
        description: Infrastracture as code provisioning.
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Ansible variables
              options:
                hosts-pattern:
                  type: Value
                  help: |
                    Ansible hosts pattern.
                    Inventory can be provided to infrared from workspace or from parameter.
                    '--inventory' can be used to load an external inventory to the workspace.
                    "--ansible-args='inventory=/path/to/inventory'" can be used to use an external
                    inventory without loading to workspace.

                    Refer to: https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html
                  required: True
                  default: 'localhost'
                  ansible_variable: 'hosts_pattern'
            - title: Binary variables
              options:
                binary-archive-url:
                    type: Value
                    help: |
                      URL to the terraform binary.
                      Every operating system and architecture has its own compiled binary.

                      Refer to: https://www.terraform.io/downloads
                    required: True
                    ansible_variable: 'binary_archive_url'

                binary-archive-sha256-checksum:
                    type: Value
                    help: |
                      SHA256 checksum of terraform binary.

                      Refer to: https://www.terraform.io/downloads
                    required: True
                    ansible_variable: 'binary_archive_sha256_checksum'

            - title: Terraform variables
              options:
                state:
                  type: Value
                  help: Terraform infrastracture state.
                  required: yes
                  choices:
                    - present
                    - absent
                  ansible_variable: 'terraform_infra_state'
                  default: 'present'

                check-mode:
                  type: Bool
                  help: |
                    Flag to check terraform plan without applying it.
                  default: False
                  required: False
                  ansible_variable: 'terraform_check_mode'

                project-path:
                  type: Value
                  help: |
                    Path to terraform project containing 'main.tf' file.

                  required: True
                  ansible_variable: 'terraform_project_path'
