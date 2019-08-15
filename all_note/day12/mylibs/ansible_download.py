import wget
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(reversed=True, type='str'),
            dest=dict(reversed=True, type='str')
                           )
    )
    wget.download(module.params['url'],module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()