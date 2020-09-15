colo evening
if has("syntax")
	syntax on
endif
set hlsearch
set nu
set autoindent
set cindent
set ts=4
set sts=4
set shiftwidth=4
set laststatus=2
set showmatch
set smartcase
set ignorecase
set smarttab
set smartindent
set ruler
set fileencodings=utf8,euc-kr,cp949
set nocompatible
map <F7> <ESC>:set mouse=a<CR>
map <F8> <ESC>:set mouse-=a<CR>
" set the runtime path to include Vundle and initialize

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

	" alternatively, pass a path where Vundle should install plugins

	"call vundle#begin('~/some/path/here')

	" let Vundle manage Vundle, required

	Plugin 'gmarik/Vundle.vim'

	" The following are examples of different formats supported.

	" Keep Plugin commands between vundle#begin/end.

	" plugin on GitHub repo

	Plugin 'tpope/vim-fugitive'

	" plugin from http://vim-scripts.org/vim/scripts.html

	Plugin 'L9'

	" Git plugin not hosted on GitHub

	Plugin 'git://git.wincent.com/command-t.git'

	" git repos on your local machine (i.e. when working on your own plugin)

	Plugin 'file:///home/gmarik/path/to/plugin'

	" The sparkup vim script is in a subdirectory of this repo called vim.

	" Pass the path to set the runtimepath properly.

	Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}

	" Vim에서 파일 탐색기를 사용할 수 있게 한다. - Nerd Tree
	"
	Plugin 'The-NERD-tree'
	"
	" " Vim에서 자동완성 기능(Ctrl + P)을 키입력하지 않더라도 자동으로
	" 나타나게 - AutoComplPop
	"
	 Plugin 'AutoComplPop'

	Plugin 'Raimondi/delimitMate'
	Plugin 'Syntastic'
	Plugin 'vim-airline/vim-airline'
	Plugin 'vim-airline/vim-airline-themes'
	

	" All of your Plugins must be added before the following line

	call vundle#end()            " required

	filetype plugin indent on    " required

	" To ignore plugin indent changes, instead use:

	"filetype plugin on

	"

	" Brief help

	" :PluginList       - lists configured plugins

	" :PluginInstall    - installs plugins; append `!` to update or just

	" :PluginUpdate

	" :PluginSearch foo - searches for foo; append `!` to refresh local cache

	" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal

	"

	" see :h vundle for more details or wiki for FAQ
let NERDTreeWinPos = "left"
nmap <C-t> :NERDTree<CR>
let delimitMate_expand_cr=1
" Syntastic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
"
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
"
let g:syntastic_cpp_compiler = 'g++'
let g:syntastic_cpp_compiler_options = "-std=c++11 -Wall -Wextra -Wpedantic"
let g:syntastic_c_compiler_options = "-std=c11 -Wall -Wextra -Wpedantic"
let g:airline#extensions#tabline#enabled = 1 " turn on buffer list
let g:airline_theme='hybrid'
set laststatus=2 " turn on bottom bar
