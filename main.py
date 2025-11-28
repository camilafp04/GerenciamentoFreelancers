from freelas import *

if __name__ == "__main__":

    gerenciamento = Gerenciamento()

    print("========================\n" \
        "Freelancers Cadastrados\n"
        "========================")
    freelancers = [
        Freelancer("Camila", 12345678910, "camila@gmail", 1312345678, "30/11/2004", "Social Midia", "Proativo", "Marketing"),
        Freelancer("Maria", 98765432111, "maria@gmail", 1309876543, "20/06/2006", "Marketing", "Criativa", "Atlética"),
        Freelancer("Lucas", 11223344556, "lucas@gmail", 1398765432, "12/07/1998", "Desenvolvimento Web", "Dedicado", "Técnico"),
        Freelancer("Julia", 99887766543, "julia@gmail", 1396543210, "02/01/1990", "Design Gráfico", "Detalhista", "Design"),
        Freelancer("Carlos", 12398745632, "carlos@gmail", 1397654321, "14/11/1995", "Consultoria", "Analítico", "Consultoria")
    ]

    for f in freelancers:
        try:
            gerenciamento.add_freelancer(f)
            print(f"Nome: {f.nome}")
        except Exception as e:
            print(f"Erro ao cadastrar {f.nome}: {e}")

    gerenciamento.listar_freelancers()

    print("\n=======================\n" \
        "Contratantes Cadastrados\n"
        "=======================")
    contratantes = [
        Contratante("Debora", 79613350055, "debora@empresa", 1397836598, "01/01/2001", 1000555426, "Empresa da Debora"),
        Contratante("Roberto", 94385689059, "roberto@tech", 1399876543, "15/03/1990", 5544100098, "Tech Solutions"),
        Contratante("Ana Clara", 29597785021, "ana@artdesign", 1398899776, "11/07/1985", 7788990044, "Arte & Design"),
    ]

    for c in contratantes:
        print(f"Contratante registrado: {c.empresa}")
        print(f"Contato: {c.email}, {c.telefone}\n")

    print("\n==================\n" \
        "Projetos Cadastrados\n"
        "==================")

    projetos = [
        Projeto(1234, "Empresa da Debora", "Social Midia", "21/12/2025", "15h30", "Cuidar das redes sociais durante evento", 200, contratantes[0]),

        Projeto(1235, "Tech Solutions", "Desenvolvimento Web", "15/11/2025", "10h00", "Desenvolver um site para e-commerce", 300, contratantes[1]),

        Projeto(1236, "Arte & Design", "Design Gráfico", "28/12/2025", "09h00","Criar identidade visual para marca", 250, contratantes[2])
    ]

    for p in projetos:
        try:
            gerenciamento.add_projeto(p)
            print(f"Projeto cadastrado: {p.titulo}")
        except Exception as e:
            print(f"Erro ao cadastrar projeto {p.titulo}: {e}")

    gerenciamento.listar_projetos()

    try:
        projetos[0].add_freelancer(freelancers[0])
        projetos[0].add_freelancer(freelancers[1])
        projetos[1].add_freelancer(freelancers[2])
        projetos[2].add_freelancer(freelancers[3])
        projetos[2].add_freelancer(freelancers[4])
    except Exception as e:
        print(f"Erro ao adicionar freelancers: {e}")

    print("\n=================================\n"
        "Projetos e freelancers associados\n"
        "=================================")

    for p in projetos:
        print("\nProjeto:\n")
        print(p)
        print("Freelancers deste projeto:")
        if p.freelancers:
            for f in p.freelancers:
                print(f"- {f.nome} ({f.atividade_principal})")
        else:
            print("Nenhum freelancer associado ainda.")