import urllib

program = ['IntelliJ', 'PyCharms', 'PhpStorm', 'Webstorm',
           'Virtual Box', 'Bitvise Client', 'Line', 'VLC',
           'Chrome', 'Fire Fox', 'WinRar', 'Sublime Text 3',
           'Draw.io', 'Java JDK', 'Python3.6', 'Python2.7',
           'Android Studio']

url = []

program_url = {
    '1' : 'https://download-cf.jetbrains.com/idea/ideaIU-2017.3.4.exe',
    '2' : 'https://download-cf.jetbrains.com/python/pycharm-professional-2017.3.4.exe',
    '3' : 'https://download-cf.jetbrains.com/webide/PhpStorm-2017.3.4.exe',
    '4' : 'https://download-cf.jetbrains.com/webstorm/WebStorm-2017.3.5.exe',
    '5' : 'https://download.virtualbox.org/virtualbox/5.1.34/VirtualBox-5.1.34-121010-Win.exe',
    '6' : 'https://dl.bitvise.com/BvSshClient-Inst.exe',
    '7' : 'https://scdn.line-apps.com/client/win/new/LineInst.exe',
    '8' : 'https://gsf-cf.softonic.com/91c/faf/411b72da616f9374835e52ba23a204b4ea/vlc-3.0.0-win32.exe?SD_used=0&channel' 
              '=WEB&fdh=no&id_file=c78b1e6e-96bf-11e6-9f04-00163ed833e7&instance=softonic_en&type=PROGRAM&url=https%3A%2F%2F' 
              'vlc-media-player.en.softonic.com&Expires=1520618827&Signature=dfBuT55dXc1ecry3XdteQFXrYQZbrH~diHl-6uBPGbxANztGrF7IG7WOV8sHzEefI' \
              '7b0qowmLsgj5g4acoN4AJ4s5juEHjWJq2igZjQOi5dcb3aZY6VoDTsXhFZ5VGjzaxlCWVOWSgGNPaErp-2XwPx-QqPDyijYGVNzjPW~xts_' 
              '&Key-Pair-Id=APKAJUA62FNWTI37JTGQ&filename=vlc-3.0.0-win32.exe',
    '9' : 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid'
               '%3D%7BF917E084-54B7-F866-212B-818048CC5706%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stabl'
               'e-statsdef_1%26installdataindex%3Ddefaultbrowser/update2/installers/ChromeSetup.exe',
    '10' : 'https://stubdownloader.cdn.mozilla.net/builds/firefox-stub/en-US/'
                 'win/24b8d5383f56fa6cb3c12d9bda3c34498c5befd92c375790752b2e52e9be1ad3/Firefox%20Installer.exe',
    '11' : 'https://www.rarlab.com/rar/winrar-x64-550.exe',
    '12' : 'https://download.sublimetext.com/Sublime%20Text%20Build%203143%20x64%20Setup.exe',
    '13' : 'https://github-production-release-asset-2e65be.s3.amazonaws.com/92443980/f88c22da-0b4c-11e8-9544-7ed6c3cef951'
                '?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180307%2Fus-east-1%2Fs3%2Faws4_'
                'request&X-Amz-Date=20180307T010924Z&X-Amz-Expires=300&X-Amz-Signature=91999cb5e261c4d0fc50286c7486499ca15f7'
                'ef3bd7adf97d90e0a1a72c7ab36&X-Amz-SignedHeaders=host&actor_id=0&response-content-dispositio'
                'n=attachment%3B%20filename%3Ddraw.io-setup-signed-8.0.6.exe&response-content-type=application%2Foctet-stream',
    '14' : 'http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-windows-x64.exe?AuthParam=1520583093_1fdb4ee3900408ff1ca9acdb941a16e7',
    '15' : 'https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64.exe',
    '16' : 'https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi',
    '17' : 'https://dl.google.com/dl/android/studio/install/3.0.1.0/android-studio-ide-171.4443003-windows.exe'
}

exe_container = []
exe_file = []


print("Enter the number of program to be installed: ")
for app in range(len(program)):
    print('{}. {}'.format(app + 1, program[app]))

pro_to_be_installed = input("Please use comma (,) to separate the input \nEnter the number: ")
# print(len(pro_to_be_installed))

if pro_to_be_installed == 0:
    for i in program_url:
        url.append(program_url['{}'.format(i)])
else:
    for num in pro_to_be_installed:
        url.append(program_url['{}'.format(num)])

count = 1
run = open('run.bat', 'w')
run.write('@echo off \n')
run.close()
print("File is downloading ......")
for link in url:
  file = urllib.urlopen(link).read()
  with open('{}.exe'.format(count), 'wb') as output:
    output.write(file)
    exe_file.append('{}.exe'.format(count))

  count += 1

print("File is written into Batch file ....")
with open('run.bat', 'a+') as app:
  for i in exe_file:
    app.write('start {} \n'.format(i))
  app.write('echo Wait until the installation finish then press then any key to continue ....\n pause >nul \n')
  for j in exe_file:
    app.write('del {} \n'.format(j))
  app.write('exit')
app.close()

print("Batch file is ready.")

# program_url = {
#     'IntelliJ' : 'https://download-cf.jetbrains.com/idea/ideaIU-2017.3.4.exe',
#     'PyCharms' : 'https://download-cf.jetbrains.com/python/pycharm-professional-2017.3.4.exe',
#     'PhpStorm' : 'https://download-cf.jetbrains.com/webide/PhpStorm-2017.3.4.exe',
#     'Webstorm' : 'https://download-cf.jetbrains.com/webstorm/WebStorm-2017.3.5.exe',
#     'Virtual Box' : 'https://download.virtualbox.org/virtualbox/5.1.34/VirtualBox-5.1.34-121010-Win.exe',
#     'Bitvise Client' : 'https://dl.bitvise.com/BvSshClient-Inst.exe',
#     'Line' : 'https://scdn.line-apps.com/client/win/new/LineInst.exe',
#     'VLC' : 'https://gsf-cf.softonic.com/91c/faf/411b72da616f9374835e52ba23a204b4ea/vlc-3.0.0-win32.exe?SD_used=0&channel'
#               '=WEB&fdh=no&id_file=c78b1e6e-96bf-11e6-9f04-00163ed833e7&instance=softonic_en&type=PROGRAM&url=https%3A%2F%2F'
#               'vlc-media-player.en.softonic.com&Expires=1520618827&Signature=dfBuT55dXc1ecry3XdteQFXrYQZbrH~diHl-6uBPGbxANztGrF7IG7WOV8sHzEefI' \
#               '7b0qowmLsgj5g4acoN4AJ4s5juEHjWJq2igZjQOi5dcb3aZY6VoDTsXhFZ5VGjzaxlCWVOWSgGNPaErp-2XwPx-QqPDyijYGVNzjPW~xts_'
#               '&Key-Pair-Id=APKAJUA62FNWTI37JTGQ&filename=vlc-3.0.0-win32.exe',
#     'Chrome' : 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid'
#                '%3D%7BF917E084-54B7-F866-212B-818048CC5706%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stabl'
#                'e-statsdef_1%26installdataindex%3Ddefaultbrowser/update2/installers/ChromeSetup.exe',
#     'Fire Fox' : 'https://stubdownloader.cdn.mozilla.net/builds/firefox-stub/en-US/'
#                  'win/24b8d5383f56fa6cb3c12d9bda3c34498c5befd92c375790752b2e52e9be1ad3/Firefox%20Installer.exe',
#     'WinRar' : 'https://www.rarlab.com/rar/winrar-x64-550.exe',
#     'Sublime Text 3' : 'https://download.sublimetext.com/Sublime%20Text%20Build%203143%20x64%20Setup.exe',
#     'Draw.io' : 'https://github-production-release-asset-2e65be.s3.amazonaws.com/92443980/f88c22da-0b4c-11e8-9544-7ed6c3cef951'
#                 '?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180307%2Fus-east-1%2Fs3%2Faws4_'
#                 'request&X-Amz-Date=20180307T010924Z&X-Amz-Expires=300&X-Amz-Signature=91999cb5e261c4d0fc50286c7486499ca15f7'
#                 'ef3bd7adf97d90e0a1a72c7ab36&X-Amz-SignedHeaders=host&actor_id=0&response-content-dispositio'
#                 'n=attachment%3B%20filename%3Ddraw.io-setup-signed-8.0.6.exe&response-content-type=application%2Foctet-stream',
#     'Java JDK' : 'http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-windows-x64.exe?AuthParam=1520583093_1fdb4ee3900408ff1ca9acdb941a16e7',
#     'Python3.6' : 'https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64.exe',
#     'Python2.7' : 'https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi'
# }