"""
-------------------------------------------------------
Comandos Básicos do Git
-------------------------------------------------------
1. git init
   Inicializa um novo repositório Git vazio.

2. git clone <url>
   Cria uma cópia local de um repositório remoto.

3. git status
   Mostra o estado atual do repositório (arquivos modificados, não rastreados, etc.).

4. git add <arquivo>
   Adiciona um ou mais arquivos à área de staging (preparando para commit).

5. git add .
   Adiciona todos os arquivos modificados e novos à área de staging.

6. git commit -m "<mensagem>"
   Faz um commit das mudanças com uma mensagem descritiva.

7. git log
   Exibe o histórico de commits do repositório.

8. git diff
   Mostra as diferenças entre arquivos ou commits.

9. git pull
   Atualiza o repositório local com as mudanças do repositório remoto.

10. git push origin <branch>
    Envia as alterações locais para o repositório remoto na branch especificada.

11. git remote add origin <url>
    Adiciona um repositório remoto (como o GitHub) ao seu repositório local.

12. git branch
    Lista, cria ou apaga branches.
    Exemplo: git branch <nome-da-branch> cria uma nova branch.

13. git checkout <branch>
    Alterna para a branch especificada.

14. git checkout -b <branch>
    Cria uma nova branch e já a faz o checkout.

15. git merge <branch>
    Mescla uma branch com a branch atual.

16. git fetch
    Baixa as mudanças do repositório remoto sem aplicá-las ao repositório local.

17. git reset
    Desfaz um commit ou alterações na área de staging.

18. git reset --hard
    Desfaz todas as mudanças, incluindo as modificações não commitadas.

19. git rm <arquivo>
    Remove arquivos do repositório e da área de staging.

20. git stash
    Guarda temporariamente as alterações não commitadas, permitindo que você volte ao estado anterior.

21. git stash pop
    Recupera e aplica as alterações guardadas com git stash.

22. git rebase <branch>
    Reaplica os commits da branch atual sobre a branch especificada, útil para atualizar branches.

23. git tag <nome-da-tag>
    Cria uma tag em um commit específico, geralmente usada para marcar versões.

24. git show <commit>
    Exibe informações detalhadas sobre um commit específico.

25. git config --global --add safe.directory '<caminho-do-repositorio>'
    Marca um diretório como seguro, permitindo que o Git funcione corretamente mesmo em diretórios com permissões especiais.
"""