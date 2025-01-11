rm -r build
rm -r dist
python3 setup.py sdist bdist_wheel


if [ "$1" == "t" ]; then
    twine upload --repository testpypi dist/*
else
    twine upload dist
fi
