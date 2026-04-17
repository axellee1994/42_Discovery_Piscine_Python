#******************************************************************************#
#                                                                              #
#                                                         :::      ::::::::    #
#    whatsyourname.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: axlee <axlee@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/17 11:05:05 by axlee             #+#    #+#              #
#    Updated: 2026/04/17 11:07:35 by axlee            ###   ########.fr        #
#                                                                              #
#******************************************************************************#

first_name = input("Hey, what's your first name? : ")
last_name = input("And your last name? : ")
whole_name = first_name + " " + last_name

def main():
    print(f"Well, pleased to meet you, {whole_name}.")

if __name__ == "__main__":
    main()
