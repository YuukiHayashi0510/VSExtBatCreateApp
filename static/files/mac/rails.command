exts = (
"VisualStudioExptTeam.vscodeintellicode"
"vscode-icons-team.vscode-icons"
)
cmd="code"
for ext in "${exts\[@\]}" ; do
	cmd="$cmd --install-extension $ext"
done
eval $cmd