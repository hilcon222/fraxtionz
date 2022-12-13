rm -rf build fraxtionz.egg-info __pycache__
cd doc
rm -rf _build
make html
dillo index.html
rm -rf _build
cd ..
python setup.py sdist bdist_wheel
twine upload dist/*
rm -rf build fraxtionz.egg-info __pycache__
git add *
git commit
git push
