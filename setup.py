from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="samwel_jumo_coding_question",
    version="0.1.0",
    description="Project for aggregating loan csv files.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="jumo coding question",
    url="https://github.com/SamwelOpiyo/Jumo-Coding-Question",
    author="Samwel Opiyo",
    author_email="samwelopiyo@example.com",
    license="MIT",
    packages=["jumo_coding_question"],
    install_requires=[],
    test_suite="nose.collector",
    tests_require=["nose"],
    entry_points={
        "console_scripts": [
            "jumo_coding_question-main=jumo_coding_question.command_line:main"
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
