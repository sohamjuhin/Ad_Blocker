import platform
import os

def block_ads():
    system = platform.system()
    hosts_path = get_hosts_path(system)
    ad_domains = get_ad_domains()
    
    if system == 'Windows':
        block_ads_windows(hosts_path, ad_domains)
    elif system == 'Darwin':
        block_ads_mac(hosts_path, ad_domains)
    elif system == 'Linux':
        block_ads_linux(hosts_path, ad_domains)
    else:
        print('Unsupported operating system.')

def unblock_ads():
    system = platform.system()
    hosts_path = get_hosts_path(system)
    ad_domains = get_ad_domains()
    
    if system == 'Windows':
        unblock_ads_windows(hosts_path, ad_domains)
    elif system == 'Darwin':
        unblock_ads_mac(hosts_path, ad_domains)
    elif system == 'Linux':
        unblock_ads_linux(hosts_path, ad_domains)
    else:
        print('Unsupported operating system.')

def get_hosts_path(system):
    if system == 'Windows':
        return 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    elif system == 'Darwin' or system == 'Linux':
        return '/etc/hosts'
    else:
        return None

def get_ad_domains():
    return [
        'ad.doubleclick.net',
        'ads.example.com',
        'adserver.example.com',
        # Add more ad domains here
    ]

def block_ads_windows(hosts_path, ad_domains):
    try:
        with open(hosts_path, 'r+') as file:
            hosts_content = file.read()
            
            for domain in ad_domains:
                if domain not in hosts_content:
                    file.write('127.0.0.1 {}\n'.format(domain))
        
        print('Ad blocking enabled.')
    except FileNotFoundError:
        print('Hosts file not found.')

def unblock_ads_windows(hosts_path, ad_domains):
    try:
        with open(hosts_path, 'r+') as file:
            hosts_lines = file.readlines()
            file.seek(0)
            
            for line in hosts_lines:
                if not any(domain in line for domain in ad_domains):
                    file.write(line)
            
            file.truncate()
        
        print('Ad blocking disabled.')
    except FileNotFoundError:
        print('Hosts file not found.')

def block_ads_mac(hosts_path, ad_domains):
    try:
        with open(hosts_path, 'r+') as file:
            hosts_content = file.read()
            
            for domain in ad_domains:
                if domain not in hosts_content:
                    file.write('127.0.0.1 {}\n'.format(domain))
        
        print('Ad blocking enabled.')
    except FileNotFoundError:
        print('Hosts file not found.')

def unblock_ads_mac(hosts_path, ad_domains):
    try:
        with open(hosts_path, 'r+') as file:
            hosts_lines = file.readlines()
            file.seek(0)
            
            for line in hosts_lines:
                if not any(domain in line for domain in ad_domains):
                    file.write(line)
            
            file.truncate()
        
        print('Ad blocking disabled.')
    except FileNotFoundError:
        print('Hosts file not found.')

def block_ads_linux(hosts_path, ad_domains):
    try:
        with open(hosts_path, 'r+') as file:
            hosts_content = file.read()
            
            for domain in ad_domains:
                if domain not in hosts_content:
                    file.write('127.0.0.1 {}\n'.format(domain))
        
        print('Ad blocking enabled.')
    except FileNotFoundError:
        print('Hosts file not found.')

def unblock_ads_linux(hosts_path, ad_domains):
    try:
        with open(hosts_path, 'r+') as file:
            hosts_lines = file.readlines()
            file.seek(0)
            
            for line in hosts_lines:
                if not any(domain in line for domain in ad_domains):
                    file.write(line)
            
            file.truncate()
        
        print('Ad blocking disabled.')
    except FileNotFoundError:
        print('Hosts file not found.')

# Example usage
block_ads()  # Enable ad blocking
# Perform web browsing
unblock_ads()  # Disable ad blocking
