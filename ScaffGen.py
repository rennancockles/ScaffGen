# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os
from glob import glob

__version__ = '1.4'

TEMPLATE_PATH = "./Templates/"
CONFIG_FILE = "./scaffConfig.json"


def get_config_data():
    with open(CONFIG_FILE) as config_file:
        config_data = json.load(config_file)
    return config_data


def get_file_content():
    with open(TEMPLATE_PATH + templateFileName, 'r') as template_file:
        file_content = template_file.read()\
            .replace("{name}", name)\
            .replace("{nameLower}", nameLower)

    return file_content


def get_final_path_name():
    if scaffoldName.lower() == 'model':
        final_name = "%s%s" % (name, extension)
    else:
        final_name = "%s%s%s" % (name, scaffoldName, extension)

    return os.path.join(destinationPath, final_name)


def write_output_file():
    create_destination_path_if_not_exists()

    with open(finalPathName, 'w') as outputFile:
        outputFile.write(str(fileContent))

    print("\nArquivo %s criado com sucesso!" % os.path.basename(finalPathName))


def create_destination_path_if_not_exists():
    if not os.path.exists(destinationPath):
        os.makedirs(destinationPath)


def get_csproj_file():
    result = []
    dir_name = destinationPath
    while len(result) == 0:
        if dir_name == "":
            return None

        result = glob(os.path.join(dir_name, "*.csproj"))
        dir_name = os.path.dirname(dir_name)

    return result[0]


def get_csproj_include_part():
    index = finalPathName.find(os.path.dirname(csprojFile))
    index += 1 + len(os.path.dirname(csprojFile))
    return finalPathName[index:]


def update_csproj():
    new_line = '    <Compile Include="%s" />\n' % csprojIncludePart

    with open(csprojFile, 'r') as f:
        csproj_content = f.read().decode("utf-8-sig", "ignore")

    if exists_in_csproj(csproj_content, new_line):
        print("%s já existe no csproj!" % csprojIncludePart)
        return

    index = csproj_content.find('    <Compile Include="%s' % os.path.dirname(csprojIncludePart))

    if index < 0:
        return

    new_content = (csproj_content[:index] + new_line + csproj_content[index:]).encode("utf-8", "ignore")

    with open(csprojFile, 'wb') as outputFile:
        outputFile.write(new_content)

    print("%s inserido no csproj com sucesso!" % csprojIncludePart)


def exists_in_csproj(content, line):
    index = content.find(line)
    return True if index >= 0 else False


def validate_name():
    if name == "":
        print("Nome inválido!")
        os.system('pause')
        exit(1)


def validate_config_exists():
    if not os.path.exists(CONFIG_FILE):
        print("Config file not found!")
        os.system('pause')
        exit(1)


def select_options():
    print("\nSelecione os modelos que deseja gerar (separados por vírgula)")
    print("\t[0] Todos")

    for i, k in enumerate(configData.keys()):
        print("\t[%d] %s" % (i+1, k))

    opts = raw_input(">> ").strip()

    try:
        opts = map(lambda o: int(o.strip()), opts.split(','))
    except:
        print("Opção inválida!")
        exit(1)

    return opts


if __name__ == '__main__':
    print("Scaffold Generator version %s\n" % __version__)

    name = raw_input("Digite um nome para criar o scaffold: ").strip()

    validate_name()
    validate_config_exists()

    nameLower = name[0].lower() + name[1:]
    configData = get_config_data()

    options = select_options()
    templates = os.listdir(TEMPLATE_PATH)

    if 0 in options:
        for templateFileName in templates:
            scaffoldName, extension = os.path.splitext(templateFileName)
            destinationPath = configData.get(scaffoldName, None)

            if extension != ".cs" or not destinationPath:
                continue

            fileContent = get_file_content()
            finalPathName = get_final_path_name()

            write_output_file()

            csprojFile = get_csproj_file()
            if not csprojFile:
                print("Arquivo csproj não encontrado!")
                continue

            csprojIncludePart = get_csproj_include_part()
            update_csproj()
    else:
        selected_templates = map(lambda o: (configData.keys()[o-1]).lower(), options)

        for templateFileName in templates:
            scaffoldName, extension = os.path.splitext(templateFileName)
            destinationPath = configData.get(scaffoldName, None)

            if scaffoldName.lower() not in selected_templates or extension != ".cs" or not destinationPath:
                continue

            fileContent = get_file_content()
            finalPathName = get_final_path_name()

            write_output_file()

            csprojFile = get_csproj_file()
            if not csprojFile:
                print("Arquivo csproj não encontrado!")
                continue

            csprojIncludePart = get_csproj_include_part()
            update_csproj()

    print("")
    os.system('pause')
