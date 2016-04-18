---
layout: chapter
title: Authenticated Forms
slides:

  - class: title-slide
    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Authenticated Forms
      _Associating form data with a user_




  - content: |

      ## Posting a message

      Only logged in user should be able to post,
      and their username should be associated.

  - content: |

      ### Allow POST data for new message route

      ```python
      @website.route('/new-message', method=['GET', 'POST'])
      @usermanager.login_required
      def new_message():
          return render_template('new-message.html')
      ```

      Add both POST and GET method options
      to the **new message** route.


  - content: |

      ### Handle both GET and POST methods

      ```python
      def new_message():

          if request.method == 'GET':
              return render_template('new-message.html')

          elif request.method == 'POST':
              return redirect('/')

      ```

      Modify the `new_message` function 
      to handle both request types.

  - content: |

      ### Get form data

  - content: |

      ### Generate current time

  - content: |

      ### Get logged in user id
  
  - content: |

      ### Write query

  - content: |

      ### Submit query with parameters
  
  - content: |

      ### Check result is valid
  
  - content: |

      ### Redirect to home page




  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Authenticated Forms: Complete!

      [Take me to the next chapter!](updating-data.html)


---