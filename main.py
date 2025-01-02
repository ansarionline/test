import nicegui.ui as ui 
ui.button(
    'Click',
    on_click=lambda:(
        ui.notify(
            'Clicked'
        )
    )
)
ui.run()