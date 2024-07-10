import glfw
import OpenGL.GL as gl

def main():
    if not glfw.init():
        raise Exception("glfw can not be initialized!")

    # 设置 OpenGL 版本和配置文件
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)  # 这对于 macOS 是必要的
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "LearnOpenGL", None, None)
    if not window:
        print("Window Creation failed!")
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, on_resize)

    while not glfw.window_should_close(window):
        process_input(window)

        # 渲染代码
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

def on_resize(window, w, h):
    gl.glViewport(0, 0, w, h)

def process_input(window):
    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

if __name__ == '__main__':
    main()
