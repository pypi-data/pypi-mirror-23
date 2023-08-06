Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Description: foto
        ====
        
        ``foto`` is **my personal** photo manager. I don't like tools pretending to be
        smarter than me. I like file-system based management and I couldn't find
        a folder-based manager which could do couple of simple tasks the way I want.
        
        Installation
        ------------
        
        Only macOS and Python 3 are supported, beause that's what I currently use.
        
        .. code:: sh
        
            $ pip install foto
        
        Also set ``FOTO_GEOCODING_API_KEY`` in your ``~/.bash_profile``.
        
        Development
        -----------
        
        .. code:: sh
        
            $ git clone git@github.com:honzajavorek/foto.git
            $ cd foto
            $ cat brew_packages.txt | xargs brew install
            $ python3 -m venv env
            $ . ./env/bin/activate
            (env)$ pip install -e .
        
        Put ``.../env/bin/foto`` into your ``~/.bash_profile`` as an alias and you're done:
        
        .. code:: sh
        
            $ echo 'alias foto=".../env/bin/foto"' >> ~/.bash_profile
        
        License: ISC
        ------------
        
        © 2010-? Honza Javorek mail@honzajavorek.cz
        
        This work is licensed under `ISC
        license <https://en.wikipedia.org/wiki/ISC_license>`__.
        
Platform: UNKNOWN
