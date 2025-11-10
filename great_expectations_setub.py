from great_expectations.data_context import FileDataContext

def setup_great_expectations_context():
    context = FileDataContext(context_root_dir="../great_expectations")
    print("Contexto configurado com sucesso!")
    return context