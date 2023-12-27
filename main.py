if __name__ == '__main__':

    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    props = [line.strip().split('=') for line in lines]
    props = {i[0].upper().replace('.', '_'): i[1] for i in props}

    envs = "; ".join([f'{i[0]}={i[1]}' for i in props.items()])
    print(envs)
