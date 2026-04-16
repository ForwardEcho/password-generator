import argparse
import string
from random import choice, sample, shuffle
import math

# ASCII Banner
banner = """
\033[1;36m
  ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
  ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
  ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
  ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
  ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
\033[1;32m
      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
     ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
     ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
     ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
     ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ 
\033[0m
\033[1;37m        [ \033[1;31mCreated by: ForwardEcho \033[1;37m]
\033[0m
"""

def generate_pwd(length, l_count, d_count, s_count):
    all_l = string.ascii_letters
    all_d = string.digits
    all_s = string.punctuation
    
    if (l_count + d_count + s_count) > length:
        return None
        
    res = []
    for _ in range(l_count):
        res.append(choice(all_l))
    for _ in range(d_count):
        res.append(choice(all_d))
    for _ in range(s_count):
        res.append(choice(all_s))
    
    rem = length - len(res)
    pool = all_l + all_d + all_s
    for _ in range(rem):
        res.append(choice(pool))
        
    shuffle(res)
    return "".join(res)

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score <= 2:
        return "\033[1;31mWeak\033[0m"
    elif score <= 4:
        return "\033[1;33mMedium\033[0m"
    else:
        return "\033[1;32mStrong\033[0m"

def brute_force_time(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in string.punctuation for c in password): pool += 32
    
    if pool == 0: pool = 1
    
    combinations = pool ** len(password)
    guesses_per_sec = 10**10 
    
    seconds = combinations / guesses_per_sec
    
    if seconds < 60:
        return f"\033[1;32m{seconds:.2f} Seconds\033[0m"
    
    minutes = seconds / 60
    if minutes < 60:
        return f"\033[1;33m{minutes:.2f} Minutes\033[0m"
        
    hours = minutes / 60
    if hours < 24:
        return f"\033[1;33m{hours:.2f} Hours\033[0m"
        
    days = hours / 24
    if days < 365:
        return f"\033[1;31m{days:.2f} Days\033[0m"
        
    years = days / 365
    if years < 1000:
        return f"\033[1;31m{years:.2f} Years\033[0m"
        
    centuries = years / 100
    return f"\033[1;35m{centuries:.2f} Centuries\033[0m"

def password_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in string.punctuation for c in password): pool += 32
    
    if pool == 0: pool = 1
    
    entropy = len(password) * math.log2(pool)
    return entropy

def main():
    print(banner)
    
    parser = argparse.ArgumentParser(description="Cybersecurity style Password Generator")
    parser.add_argument("-l", "--length", type=int, required=True, help="Total length of the password")
    parser.add_argument("-n", "--number", type=int, required=True, help="Number of passwords to generate")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output file name")
    parser.add_argument("-s", "--special", type=int, required=True, help="Minimum special characters")
    parser.add_argument("-d", "--digits", type=int, required=True, help="Minimum digits")
    parser.add_argument("-a", "--letters", type=int, required=True, help="Minimum letters")

    args = parser.parse_args()

    passwords = []
    for _ in range(args.number):
        pwd = generate_pwd(args.length, args.letters, args.digits, args.special)
        if pwd:
            passwords.append(pwd)
        else:
            print("\033[1;31m[!] Error: Total requested characters exceed total length.\033[0m")
            return

    try:
        with open(args.output, "w") as f:
            for p in passwords:
                f.write(p + "\n")
        
        if passwords:
            print(f"\033[1;36m[#] Sample:\033[0m {passwords[0]}")
            print(f"\033[1;36m[#] Entropy:\033[0m {password_entropy(passwords[0])}")
            print(f"\033[1;36m[#] Strength:\033[0m {password_strength(passwords[0])}")
            print(f"\033[1;36m[#] Crack Time:\033[0m {brute_force_time(passwords[0])}")
        print(f"\033[1;32m[+]\033[0m Successfully generated {len(passwords)} passwords!")
        print(f"\033[1;32m[+]\033[0m Saved to: \033[1;34m{args.output}\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Error writing file: {e}\033[0m")

if __name__ == "__main__":
    main()