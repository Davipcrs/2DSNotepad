; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "2D - Bloco de Notas"
#define MyAppVersion "Beta 0.1"
#define MyAppPublisher "2D Software"
#define MyAppURL "https://www.2dpersonalizados.com.br/blocodenotas"
#define MyAppExeName "2DSNotepad.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{8920BBAF-B781-4AAD-B3B5-0BA37015F77E}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\2DSNotepad
DisableProgramGroupPage=yes
LicenseFile=C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\license\LICENSE.txt
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\davip\Desktop\teste
OutputBaseFilename=2DSNotepad_setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\_decimal.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\libcrypto-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\libssl-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\python39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\VCRUNTIME140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\davip\Documents\Projetos\2DpsNotes\dist\2DSNotepad\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

