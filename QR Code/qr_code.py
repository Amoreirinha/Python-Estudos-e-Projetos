import qrcode
from qrcode.image.pil import PilImage
import os

data = input('Informação do QR Code:\n')
border_img = input('Selecione um valor para a borda do QR Code:\n')
box_s = input('Selecione um valor para o tamanho da imagem:\n')
save = input('Selecione onde salvar o QR Code (endereço da pasta) ou deixe em branco para salvar na pasta atual:\n')

cores = {
    '1': (0, 0, 0),         
    '2': (255, 255, 255),   
    '3': (255, 0, 0),
    '4': (0, 0, 255),
    '5': (200, 162, 200),
    '6': (255, 0, 255),
    '7': (0, 255, 0),
    '8': (255, 255, 0),
    '9': (128, 0, 128),
    '10': (255, 192, 203),
    '11': (255, 165, 0),
    '12': (139, 69, 19),
    '13': (0, 0, 139),
    '14': (80, 200, 120),
}

nome_cor = {
    '1': 'Preto',
    '2': 'Branco',
    '3': 'Vermelho',
    '4': 'Azul',
    '5': 'Lilás',
    '6': 'Magenta',
    '7': 'Verde',
    '8': 'Amarelo',
    '9': 'Roxo',
    '10': 'Rosa',
    '11': 'Laranja',
    '12': 'Marrom',
    '13': 'Azul Escuro',
    '14': 'Verde Esmeralda',
}

# Função para exibir opções de cores
def exibir_opcoes(nome_cor):
    print('Opções de cores:')
    for key, value in nome_cor.items():
        print(f'{key} - {value}')

# Seleção de cores
exibir_opcoes(nome_cor)
color_back = input('Selecione a cor de fundo (número):\n')
color_fill = input('Selecione a cor principal do QR Code (número):\n')

# Verificação se as cores são diferentes
if color_back == color_fill:
    print("A cor de fundo não pode ser igual à cor principal.")
else:
    confirmar1 = input(f'Informação do QR Code: {data}\nTamanho da Borda: {border_img}\n'
                       f'Tamanho do QR Code: {box_s}\nCor de Fundo: {nome_cor[color_back]}\nCor Principal: {nome_cor[color_fill]}\n'
                       f'Local de salvamento: {save if save else "Pasta atual"}\n'
                       f'\nConfirmar valores inseridos? Digite "s" para sim e "n" para não...\n')

    if confirmar1 == 's':
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=int(box_s),
            border=int(border_img)
        )
        
        qr.add_data(data)
        qr.make(fit=True)
        
        # Obtendo as cores selecionadas
        fill_color = cores[color_fill]
        back_color = cores[color_back]
        
        # Verificação e ajuste do caminho de salvamento
        if not save:
            save = os.getcwd()  # Caminho da pasta atual
        if not save.endswith('/') and not save.endswith('\\'):
            save += os.sep
        
        # Criando e salvando a imagem do QR Code
        img = qr.make_image(fill_color=fill_color, back_color=back_color, image_factory=PilImage)
        img.save(os.path.join(save, str(data) + '.png'))
        print("QR Code gerado com sucesso!")
    else:
        print("Operação cancelada.")
print('Adeus')