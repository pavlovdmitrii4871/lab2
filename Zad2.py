from deq_stack import Dequeue

def decrypt_message(msg, deck):
    decrypted_msg = ''
    for char in msg:
        while True:
            curr = deck.pop_last()
            deck.push_first(curr)
            if curr == char:
                deck.push_first(deck.pop_last())
                cc = deck.pop_last()
                decrypted_msg += cc
                deck.push_first(cc)
                break
    return decrypted_msg

def main():
    filename = "ABC.txt"
    with open(filename, 'r') as file:
        encrypted_msg = file.read()
    deck = Dequeue()
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        deck.push_last(c)
    decrypted_msg = decrypt_message(encrypted_msg, deck)
    print("Расшифрованное сообщение:")
    print(decrypted_msg)
    with open("decrypted.txt", 'w') as file:
        file.write(decrypted_msg)

if __name__ == "__main__":
    main()
