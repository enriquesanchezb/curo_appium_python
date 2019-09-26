# Curso Appium

## Slides
https://www.dropbox.com/s/y71a1xx0rgj55fx/Understanding%20Appium.pdf?dl=0

## Instrucciones del Curso

Instala NodeJS
- Windows: https://www.guru99.com/download-install-node-js.html
- Linux/Mac: https://nodejs.org/es/download/package-manager/

Instala Java y setea JAVA_HOME
- Windows: https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/
- Linux: https://www.guru99.com/how-to-install-java-on-ubuntu.html
- Mac: https://www.mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/

Si usas  Mac OS X
- Instala Xcode https://itunes.apple.com/es/app/xcode/id497799835?mt=12
- Instala Xcode Build Tools https://railsapps.github.io/xcode-command-line-tools.html

Instala Android SDK
- https://www.xatakandroid.com/programacion-android/como-instalar-el-android-sdk-y-para-que-nos-sirve

Instala un emulador
- https://developer.android.com/studio/run/managing-avds?hl=es-419

Instala Appium Desktop
- https://github.com/appium/appium-desktop/releases/tag/v1.13.0

Puedes chequear que todo está instalado ejecutando appium-doctor
- https://github.com/appium/appium-doctor

## Instalar Python3
https://python-guide-es.readthedocs.io/es/latest/starting/install3/linux.html

### Instalar dependencias para el proyecto

```
pip3 install pipenv #install pipenv 
pipenv install
```

## Ejecutar los test

- Ten levantado Appium Desktop
- Asegúrate de tener un emulador de Android o un dispositivo Android conectado al ordenador
- Ejecuta los siguientes comandos en tu terminal
```
pipenv run pytest
```