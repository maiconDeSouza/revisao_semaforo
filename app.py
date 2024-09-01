import json
import os
import platform
import time
import random
path = './db_revisao.json'


def create_data_base():
    with open(path, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)


def salve_data_base(db):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)


def load_json():
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_new_note():
    print('Digite o id da nota:')
    id = input()
    print('Digite o nome da tarefa:')
    name = input()
    new_note = {
        'id': id,
        'name': name,
        'semaphore': 'vermelho'
    }
    return new_note


def review_note(db):
    notes_red = filter(lambda note: note['semaphore'] == 'vermelho', db)
    notes_red_list = list(notes_red)

    if len(notes_red_list):
        random_note = random.sample(notes_red_list, 1)

        while True:
            print('\n')
            message(random_note)
            print("Depois que revisar a nota, digite:")
            print("vermelho")
            print("amarelo")
            print("verde")
            semaphore = input()
            if semaphore != 'vermelho' and semaphore != 'amarelo' and semaphore != 'verde':
                message('Digite um valor valido!')
                continue
            else:
                for note in db:
                    if note['id'] == random_note[0]['id']:
                        note['semaphore'] = semaphore
                        salve_data_base(db)
                        break
                break
        return

    notes_yellow = filter(lambda note: note['semaphore'] == 'amarelo', db)
    notes_yellow_list = list(notes_yellow)

    if len(notes_yellow_list):
        random_note = random.sample(notes_yellow_list, 1)

        while True:
            print('\n')
            message(random_note)
            print("Depois que revisar a nota, digite:")
            print("vermelho")
            print("amarelo")
            print("verde")
            semaphore = input()
            if semaphore != 'vermelho' and semaphore != 'amarelo' and semaphore != 'verde':
                message('Digite um valor valido!')
                continue
            else:
                for note in db:
                    if note['id'] == random_note[0]['id']:
                        note['semaphore'] = semaphore
                        salve_data_base(db)
                        break
                break
        return

    notes_green = filter(lambda note: note['semaphore'] == 'verde', db)
    notes_green_list = list(notes_green)

    if len(notes_green_list):
        random_note = random.sample(notes_green_list, 1)

        while True:
            print('\n')
            message(random_note)
            print("Depois que revisar a nota, digite:")
            print("vermelho")
            print("amarelo")
            print("verde")
            semaphore = input()
            if semaphore != 'vermelho' and semaphore != 'amarelo' and semaphore != 'verde':
                message('Digite um valor valido!')
                continue
            else:
                for note in db:
                    if note['id'] == random_note[0]['id']:
                        note['semaphore'] = semaphore
                        salve_data_base(db)
                        break
                break
        return


def number_of_notes(db):
    red = list(filter(lambda note: note['semaphore'] == 'vermelho', db))
    yellow = list(filter(lambda note: note['semaphore'] == 'amarelo', db))
    green = list(filter(lambda note: note['semaphore'] == 'verde', db))

    message_return = {
        "vermelho": len(red),
        "amarelo": len(yellow),
        "verde": len(green)
    }
    return message_return


def message(message):
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print(message)
    time.sleep(2)


def menu(option, db):
    if option == '1':
        new_note = create_new_note()
        db.append(new_note)
        salve_data_base(db)
        message_return = f'Nota Criada vom sucesso, {new_note}'
        message(message_return)
        return True
    elif option == '2':
        review_note(db)
        message_return = 'Revisada com sucesso!'
        message(message_return)
        return True
    elif option == '3':
        message_return = number_of_notes(db)
        message(message_return)
        return True
    elif option == '4':
        message_return = 'Bye'
        message(message_return)
        return False
    else:
        message("Opção inválida. Tente novamente.")

        return True


def main():
    program_running = True
    if not os.path.exists(path):
        create_data_base()

    db = load_json()

    while program_running:
        print("\n### Menu ###")
        print("1. Cadastrar nova nota")
        print("2. Revisar notas")
        print("3. Mostrar quantidade de notas")
        print("4. Sair")

        option = input()
        program_running = menu(option, db)


if __name__ == "__main__":
    main()
