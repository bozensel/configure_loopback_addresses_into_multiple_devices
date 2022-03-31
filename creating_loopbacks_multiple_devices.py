from netmiko import ConnectHandler

ports = [21211, 21212, 21214, 21215, 21216]

for port in ports:

    SR_7_3_ssh = {
        'device_type': 'alcatel_sros',
        'ip': '135.243.92.118',
        'username': 'admin',
        'password': 'admin',
        'port': port
    }

    net_connect = ConnectHandler(**SR_7_3_ssh)
    output = net_connect.send_command('show router interf')
    print (output)
    i = 1
    while i < 100:
        config_commands = ['configure', 'router interface lo' + str(i), 'address 1.1.1.' + str(i) + '/32', 'loopback']
        output = net_connect.send_config_set(config_commands)
        i = i + 1
    print (output)

# The sample output from the code:

'''
configure 
*A:K1>config# router interface "lo99"
*A:K1>config>router>if# address 1.1.1.99/32
*A:K1>config>router>if# loopback
*A:K1>config>router>if# exit all
*A:K1#

===============================================================================
Interface Table (Router: Base)
===============================================================================
Interface-Name                   Adm         Opr(v4/v6)  Mode    Port/SapId
   IP-Address                                                    PfxState
-------------------------------------------------------------------------------
lo1                              Up          Up/Down     Network loopback
   1.1.1.1/32                                                    n/a
lo10                             Up          Up/Down     Network loopback
   1.1.1.10/32                                                   n/a
lo11                             Up          Up/Down     Network loopback
   1.1.1.11/32                                                   n/a
lo12                             Up          Up/Down     Network loopback
   1.1.1.12/32                                                   n/a
lo13                             Up          Up/Down     Network loopback
   1.1.1.13/32                                                   n/a
lo14                             Up          Up/Down     Network loopback
   1.1.1.14/32                                                   n/a
lo15                             Up          Up/Down     Network loopback
   1.1.1.15/32                                                   n/a
lo16                             Up          Up/Down     Network loopback
   1.1.1.16/32                                                   n/a
lo17                             Up          Up/Down     Network loopback
   1.1.1.17/32                                                   n/a
lo18                             Up          Up/Down     Network loopback
   1.1.1.18/32                                                   n/a
'''
    
