name: Bug report
description: Report a bug with this package.
labels: bug
body:
  test text
  - type: markdown
    attributes:
      value: |
        Please note that only issues related to the installation of this package should be reported here. For issues that are not related to the conda-forge process, please contact the maintainers of the package.

  - type: checkboxes
    id: documentation
    attributes:
      label: Solution to issue cannot be found in the documentation.
      description: |
        I read [the conda-forge documentation](https://conda-forge.org/docs/user/introduction.html#how-can-i-install-packages-from-conda-forge) and could not find the solution for my problem there.
      options:
        - label: I checked the documentation.
          required: true

  - type: textarea
    id: Issue
    attributes:
      label: Issue
      description: |
        Please describe the issue you are experiencing:
    validations:
      required: true

  - type: textarea
    id: environment
    attributes:
      label: Installed packages
      description: |
        Please share your installed packages by running `conda list` and entering the output below:
        _Note:_ This will be automatically formatted as code.
      placeholder: "conda list"
      render: shell
    validations:
      required: true

  - type: textarea
    id: info
    attributes:
      label: Environment info
      description: |
        Please share your environment by running `conda info` and entering the output below:
        _Note:_ This will be automatically formatted as code.
      placeholder: "conda info"
      render: shell
    validations:
      required: true
