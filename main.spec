# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=['/caminho/para/o/projeto'],
    binaries=[],
    datas=[
        ('app/screens/screenmanager.kv', 'app/screens'),
        ('app/screens/login_screen/loginscreen.kv', 'app/screens/login_screen'),
        ('app/screens/tela_principal/telaprincipal.kv', 'app/screens/tela_principal'),
        ('app/screens/cadastro/cadastroCliente.kv', 'app/screens/cadastro'),
        ('app/screens/cadastro/cadastroService.kv', 'app/screens/cadastro'),
        ('app/screens/cadastro/newService.kv', 'app/screens/cadastro'),
        ('app/screens/consulta/consultaCliente.kv', 'app/screens/consulta'),
        ('app/screens/consulta/consultaService.kv', 'app/screens/consulta'),
        ('app/screens/consulta/consultaOrcamento.kv', 'app/screens/consulta'),
        ('app/screens/consulta/consultaUnica.kv', 'app/screens/consulta'),
        ('app/screens/alterar/alterarCliente.kv', 'app/screens/alterar'),
        ('app/screens/alterar/alterarService.kv', 'app/screens/alterar'),
        ('app/screens/alterar/alterarRegistro.kv', 'app/screens/alterar'),
        ('app/screens/deletar/deletarCliente.kv', 'app/screens/deletar'),
        ('app/screens/deletar/deletarServico.kv', 'app/screens/deletar'),
        ('app/screens/deletar/deletarOrcamento.kv', 'app/screens/deletar'),
        ('app/support/fonts/monofonto.otf', 'app/support/fonts')
    ],
    hiddenimports=[
        'app.screens.screenmanager',
        'app.screens.login_screen.loginscreen',
        'app.screens.tela_principal.telaprincipal',
        'app.screens.cadastro.cadastroCliente',
        'app.screens.cadastro.cadastroService',
        'app.screens.cadastro.newService',
        'app.screens.consulta.consultaCliente',
        'app.screens.consulta.consultaService',
        'app.screens.consulta.consultaOrcamento',
        'app.screens.consulta.consultaUnica',
        'app.screens.alterar.alterarCliente',
        'app.screens.alterar.alterarService',
        'app.screens.alterar.alterarRegistro',
        'app.screens.deletar.deletarCliente',
        'app.screens.deletar.deletarServico',
        'app.screens.deletar.deletarOrcamento'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
