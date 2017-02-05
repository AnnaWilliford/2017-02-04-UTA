# Introduction to Git

Note: Students must have Git installed and must have created a GitHub account.

1. Describing Git
    - Version control system
    - Allows user to keep track of files and versions of files
    - Much like Google Docs, where you can view a history and go back, if needed
    - Also great for collaboration
    - And for sharing

2. Setting up Git (5 minutes)
    - Git commands are written as `get <verb> <parameters>`
    - Set up global configuration:
        * User name -- `git config --global user.name "Your name"`
        * User email -- `git config --global user.email "your@email.com"`
        * Colored output -- `git config --global color.ui "auto"`
        * Editor -- `git config --global core.editor "nano -w"`
     - specify text editor, to be used in committing
        * nano: `git config --global core.editor "nano -w"`
        * text wrangler: `git config --global core.editor "edit -w"`
        * notepad++: `git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`
        * kate: `git config --global core.editor "kate"`
    - Access help with `git <command> -h/--help`

3. Creating a repository (10 minutes)
    - Enter directory where python scripts are stored
    - Initialize repository -- `git init`
    - `ls -a` -- Everything git-related lives in the `.git` directory.
    - Print status -- `git status`
    - Caution against nesting repositories
        * _Can_ do it with submodules, but that's a very advanced topic

4. Tracking changes (20 minutes)
    - The three locations of Git:
        - Working directory -- files that are entirely local and have no backup. Anything in here that is not in Git is easily lost.
        - Staging area -- files that are ready to be added to Git, but have not been added yet
        - Repository -- snapshots of files that are within Git's system and therefore 'safe'. You have lots of powerful access to this.
    - Corresponding commands:
        - `git add` adds files that have been changed in the working directory to the staging area. 
        - `git commit` moves all files in the staging area to the repository
    - Add and commit (`commit -m 'your message'`) first file
    - `git status` -- should show there are still many "untracked" files, but the script we added isn't one of them
    - `git log` -- shows history of changes
        - Aside on paging (`less`) -- navigate with arrows, quit with `q`
    - Add some comments to the script
        - `git status` -- should show that the script has been changed
        - `git diff` -- shows exactly how you changed the file since the last commit
        - `git add` to add the change, and then `git diff` vs. `git diff --staged` to view the changes
        - `git status` to show what's staged
        - Commit the change

5. Intro to Markdown
    - Markdown is a syntax that allows you to write plain text files, which get rendered into stylized documents
    - Best way to learn is by doing, using a guide that makes it easy to understand: [https://guides.github.com/features/mastering-markdown/](https://guides.github.com/features/mastering-markdown/)
    - We can incorporate Markdown into our Jupyter Notebooks to help provide more of a narrative, so let's do that
    - Create a new Jupyter Notebook called `demography_analysis_report`
    -**Challenge:** Get familiar with Markdown syntax and write the outline of a report on the data analysis we've done over the last couple days: introduction (what do you want to know?), methods (what did you do to figure it out?), results (what did you find?), and conclusion (what does your result mean?). Put each section in its own block. Once you are happy, commit your change using Git.

6. Remotes in GitHub (30 minutes)
    - Set up a GitHub account
    - Create a blank repository
    - `git remote add origin <URL>`
        - Test that it worked -- `git remote -v`
        - More robust test -- `git remote show origin`
        - `origin` is an arbitrary name for the remote -- you can call it whatever you want, but `origin` happens to be a very common name for your personal remote.
        - You can create multiple remotes -- we will touch on this in the next section ("Collaborating")
    - Upload changes to the repository -- `git push origin master`
        - `master` is the name of the `branch` you are on. Branches are a more advanced git feature that is covered in a different SWC lesson. All you need to know is that, unless you create any new branches, the default branch is always called `master`
    - Now that our changes have been committed, we can push them online to GitHub with `git push origin master`
    - Go to your repository on GitHub and view the `demographic_analysis_report` Markdown document that you created. Notice the formating that has appeared as your Markdown gets rendered.
    - Let's finish by having you go back to your report document. You've created a narrative using Markdown. Now let's insert back in the important code so that we can view more details about what happened.
    - Take a look at the `demographic_analysis_report.ipynb` to see a working examples of what a Jupyter notebook report could look like.
