let s:cpo_save=&cpo
set cpo&vim
cnoremap <silent> <Plug>(TelescopeFuzzyCommandSearch) e "lua require('telescope.builtin').command_history { default_text = [=[" . escape(getcmdline(), '"') . "]=] }"
imap <C-G>S <Plug>ISurround
imap <C-G>s <Plug>Isurround
imap <C-S> <Plug>Isurround
inoremap <silent> <C-Tab> =UltiSnips#ListSnippets()
imap <silent> <S-Tab> <Plug>(TaboutBack)
inoremap <Plug>(TaboutBackMulti) <Cmd>lua require("tabout").taboutBackMulti()
inoremap <Plug>(TaboutBack) <Cmd>lua require("tabout").taboutBack()
inoremap <Plug>(TaboutMulti) <Cmd>lua require("tabout").taboutMulti()
inoremap <Plug>(Tabout) <Cmd>lua require("tabout").tabout()
inoremap <C-W> u
inoremap <C-U> u
snoremap <silent>  "_c
xnoremap <silent> 	 :call UltiSnips#SaveLastVisualSelection()gvs
snoremap <silent> 	 :call UltiSnips#ExpandSnippetOrJump()
nnoremap  <Cmd>nohlsearch|diffupdate|normal! 
snoremap  "_c
nmap  d
nnoremap <silent>  <Left> :bprev
nnoremap <silent>  <Right> :bnext
nnoremap <silent>  x :bd
nnoremap <silent>  e :NvimTreeToggle
nnoremap <silent>  fg :Telescope live_grep
nnoremap <silent>  ff :Telescope find_files
nnoremap <silent>  v :VimtexView
nnoremap <silent>  co :VimtexCompile
vnoremap  pp "+p
nnoremap  pp "+p
vnoremap  y "+yy
nnoremap  y "+yy
omap <silent> % <Plug>(MatchitOperationForward)
xmap <silent> % <Plug>(MatchitVisualForward)
nmap <silent> % <Plug>(MatchitNormalForward)
nnoremap & :&&
onoremap <silent> , <Plug>Lightspeed_,_ft
xnoremap <silent> , <Plug>Lightspeed_,_ft
nnoremap <silent> , <Plug>Lightspeed_,_ft
onoremap <silent> ; <Plug>Lightspeed_;_ft
xnoremap <silent> ; <Plug>Lightspeed_;_ft
nnoremap <silent> ; <Plug>Lightspeed_;_ft
xnoremap <silent> <expr> @ mode() ==# 'V' ? ':normal! @'.getcharstr().'' : '@'
onoremap <silent> F <Plug>Lightspeed_F
xnoremap <silent> F <Plug>Lightspeed_F
nnoremap <silent> F <Plug>Lightspeed_F
xnoremap <silent> <expr> Q mode() ==# 'V' ? ':normal! @=reg_recorded()' : 'Q'
nnoremap <silent> S <Plug>Lightspeed_S
xmap S <Plug>VSurround
onoremap <silent> T <Plug>Lightspeed_T
xnoremap <silent> T <Plug>Lightspeed_T
nnoremap <silent> T <Plug>Lightspeed_T
onoremap <silent> X <Plug>Lightspeed_X
nnoremap Y y$
onoremap <silent> Z <Plug>Lightspeed_S
omap <silent> [% <Plug>(MatchitOperationMultiBackward)
xmap <silent> [% <Plug>(MatchitVisualMultiBackward)
nmap <silent> [% <Plug>(MatchitNormalMultiBackward)
omap <silent> ]% <Plug>(MatchitOperationMultiForward)
xmap <silent> ]% <Plug>(MatchitVisualMultiForward)
nmap <silent> ]% <Plug>(MatchitNormalMultiForward)
xmap a% <Plug>(MatchitVisualTextObject)
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nmap ds <Plug>Dsurround
onoremap <silent> f <Plug>Lightspeed_f
xnoremap <silent> f <Plug>Lightspeed_f
nnoremap <silent> f <Plug>Lightspeed_f
nmap gcu <Plug>Commentary<Plug>Commentary
nnoremap <silent> gS <Plug>Lightspeed_gS
nnoremap <silent> gs <Plug>Lightspeed_gs
xmap gS <Plug>VgSurround
omap <silent> g% <Plug>(MatchitOperationBackward)
xmap <silent> g% <Plug>(MatchitVisualBackward)
nmap <silent> g% <Plug>(MatchitNormalBackward)
omap gc <Plug>Commentary
nmap gcc <Plug>CommentaryLine
xmap gc <Plug>Commentary
nmap gc <Plug>Commentary
xnoremap <silent> s <Plug>Lightspeed_s
nnoremap <silent> s <Plug>Lightspeed_s
onoremap <silent> t <Plug>Lightspeed_t
onoremap <silent> x <Plug>Lightspeed_x
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
onoremap <silent> z <Plug>Lightspeed_s
nmap <silent> <Plug>CommentaryUndo :echoerr "Change your <Plug>CommentaryUndo map to <Plug>Commentary<Plug>Commentary"
nnoremap <Plug>PlenaryTestFile :lua require('plenary.test_harness').test_file(vim.fn.expand("%:p"))
nnoremap <silent> <Plug>SurroundRepeat .
snoremap <C-R> "_c
snoremap <silent> <C-H> "_c
snoremap <silent> <Del> "_c
snoremap <silent> <BS> "_c
snoremap <silent> <C-Tab> :call UltiSnips#ListSnippets()
xmap <silent> <Plug>(MatchitVisualTextObject) <Plug>(MatchitVisualMultiBackward)o<Plug>(MatchitVisualMultiForward)
onoremap <silent> <Plug>(MatchitOperationMultiForward) :call matchit#MultiMatch("W",  "o")
onoremap <silent> <Plug>(MatchitOperationMultiBackward) :call matchit#MultiMatch("bW", "o")
xnoremap <silent> <Plug>(MatchitVisualMultiForward) :call matchit#MultiMatch("W",  "n")m'gv``
xnoremap <silent> <Plug>(MatchitVisualMultiBackward) :call matchit#MultiMatch("bW", "n")m'gv``
nnoremap <silent> <Plug>(MatchitNormalMultiForward) :call matchit#MultiMatch("W",  "n")
nnoremap <silent> <Plug>(MatchitNormalMultiBackward) :call matchit#MultiMatch("bW", "n")
onoremap <silent> <Plug>(MatchitOperationBackward) :call matchit#Match_wrapper('',0,'o')
onoremap <silent> <Plug>(MatchitOperationForward) :call matchit#Match_wrapper('',1,'o')
xnoremap <silent> <Plug>(MatchitVisualBackward) :call matchit#Match_wrapper('',0,'v')m'gv``
xnoremap <silent> <Plug>(MatchitVisualForward) :call matchit#Match_wrapper('',1,'v'):if col("''") != col("$") | exe ":normal! m'" | endifgv``
nnoremap <silent> <Plug>(MatchitNormalBackward) :call matchit#Match_wrapper('',0,'n')
nnoremap <silent> <Plug>(MatchitNormalForward) :call matchit#Match_wrapper('',1,'n')
nmap <C-W><C-D> d
nnoremap <C-L> <Cmd>nohlsearch|diffupdate|normal! 
imap S <Plug>ISurround
imap s <Plug>Isurround
inoremap <silent> 	 =UltiSnips#ExpandSnippetOrJump()
imap  <Plug>Isurround
inoremap  u
inoremap  u
let &cpo=s:cpo_save
unlet s:cpo_save
set grepformat=%f:%l:%c:%m
set grepprg=rg\ --vimgrep\ -uu\ 
set helplang=en
set packpath=/opt/homebrew/Cellar/neovim/0.10.1/share/nvim/runtime
set runtimepath=~/.local/share/nvim/pckr/pckr.nvim,~/.config/nvim,~/.local/share/nvim/site,/opt/homebrew/Cellar/neovim/0.10.1/share/nvim/runtime,/opt/homebrew/Cellar/neovim/0.10.1/share/nvim/runtime/pack/dist/opt/matchit,/opt/homebrew/Cellar/neovim/0.10.1/lib/nvim,~/.local/share/nvim/site/pack/pckr/opt/ultisnips,~/.local/share/nvim/site/pack/pckr/opt/vim-surround,~/.local/share/nvim/site/pack/pckr/opt/obsidian.nvim,~/.local/share/nvim/site/pack/pckr/opt/tabout.nvim,~/.local/share/nvim/site/pack/pckr/opt/lightspeed.nvim,~/.local/share/nvim/site/pack/pckr/opt/plenary.nvim,~/.local/share/nvim/site/pack/pckr/opt/nvim,~/.local/share/nvim/site/pack/pckr/opt/nvim-web-devicons,~/.local/share/nvim/site/pack/pckr/opt/nvim-treesitter,~/.local/share/nvim/site/pack/pckr/opt/nvim-tree.lua,~/.local/share/nvim/site/pack/pckr/opt/vim-auto-save,~/.local/share/nvim/site/pack/pckr/opt/vim-commentary,~/.local/share/nvim/site/pack/pckr/opt/nui.nvim,~/.local/share/nvim/site/pack/pckr/opt/autoclose.nvim,~/.local/share/nvim/site/pack/pckr/opt/lualine.nvim,~/.local/share/nvim/site/pack/pckr/opt/kanagawa.nvim,~/.local/share/nvim/site/pack/pckr/opt/vimtex,~/.local/share/nvim/site/pack/pckr/opt/telescope.nvim,~/.local/share/nvim/site/pack/pckr/opt/vimtex/after,~/.local/share/nvim/site/pack/pckr/opt/nvim/after,~/.local/share/nvim/site/pack/pckr/opt/ultisnips/after
set scrolloff=30
set statusline=%#Normal#
set termguicolors
set undodir=~/.nvim/undodir
set undofile
set window=44
" vim: set ft=vim :
