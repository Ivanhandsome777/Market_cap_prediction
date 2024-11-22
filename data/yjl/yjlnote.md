conda create -n yjlhandsome python=3.8
conda env list
activate yjlhandsome
cd pojectfold balaabanbab
pip install -r requirements.txt
pip list
conda env export > environment.yml
ctrl shift v open md
这个提示是因为 Git 需要你配置用户名和邮箱地址，以便在提交代码时标记提交者身份。你可以按照以下步骤在 VS Code 的终端中进行设置：

1. 打开 VS Code 的终端（快捷键：`Ctrl + ``）。
2. 输入以下命令，将 `Your Name` 和 `your.email@example.com` 替换为你的实际信息。

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

   这些设置会在全局范围内生效。如果你只希望对当前项目生效，可以去掉 `--global`。

3. 配置完成后，重新尝试你的 Git 操作，错误提示应该消失了。

这一步是必要的，因为 Git 需要知道提交的用户名和邮箱才能跟踪代码的历史变更和责任人。

yml文件里面要写 conda-forge 还要删除掉prefix

page=request.args.get("page",default=1,type=int)

C:\Users\jlgmp\anaconda3
C:\Users\jlgmp\anaconda3\Scripts
C:\Users\jlgmp\anaconda3\Library\lib
C:\Users\jlgmp\anaconda3\Library\mingw-w64\bin