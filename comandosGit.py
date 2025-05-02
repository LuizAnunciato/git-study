"""
-------------------------------------------------------
Comandos Básicos do Git
-------------------------------------------------------
git init
Inicializa um novo repositório Git vazio.

git clone <url>
Cria uma cópia local de um repositório remoto.

git status
Mostra o estado atual do repositório (arquivos modificados, não rastreados, etc.).

git add <arquivo>
Adiciona um ou mais arquivos à área de staging (preparando para commit).

git add .
Adiciona todos os arquivos modificados e novos à área de staging.

git commit -m "<mensagem>"
Faz um commit das mudanças com uma mensagem descritiva.

git log
Exibe o histórico de commits do repositório.

git diff
Mostra as diferenças entre arquivos ou commits.

git pull
Atualiza o repositório local com as mudanças do repositório remoto.

git push origin <branch>
Envia as alterações locais para o repositório remoto na branch especificada.

git remote add origin <url>
Adiciona um repositório remoto (como o GitHub) ao seu repositório local.

git branch
Lista, cria ou apaga branches.

Exemplo: git branch <nome-da-branch> cria uma nova branch.

git checkout <branch>
Alterna para a branch especificada.

git checkout -b <branch>
Cria uma nova branch e já a faz o checkout.

git merge <branch>
Mescla uma branch com a branch atual.

git fetch
Baixa as mudanças do repositório remoto sem aplicá-las ao repositório local.

git reset
Desfaz um commit ou alterações na área de staging.

git reset --hard desfaz todas as mudanças, incluindo as modificações não commitadas.

git rm <arquivo>
Remove arquivos do repositório e da área de staging.

git stash
Guarda temporariamente as alterações não commitadas, permitindo que você volte ao estado anterior.

git stash pop
Recupera e aplica as alterações guardadas com git stash.

git rebase <branch>
Reaplica os commits da branch atual sobre a branch especificada, útil para atualizar branches.

git tag <nome-da-tag>
Cria uma tag em um commit específico, geralmente usada para marcar versões.

git show <commit>
Exibe informações detalhadas sobre um commit específico.

"""