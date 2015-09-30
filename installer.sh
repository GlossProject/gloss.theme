wget https://launchpad.net/plone/5.0/5.0/+download/Plone-5.0-UnifiedInstaller.tgz
tar xvfz Plone-5.0-UnifiedInstaller.tgz
cd Plone-5.0-UnifiedInstaller
tar xfj packages/buildout-cache.tar.bz2 
mv buildout-cache/eggs/ ../
rm -rf buildout-cache
cd ..
rm -rf Plone-5.0-UnifiedInstaller*
