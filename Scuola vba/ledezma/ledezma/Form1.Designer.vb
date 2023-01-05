<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.lstnm = New System.Windows.Forms.ListBox()
        Me.lstGa = New System.Windows.Forms.ListBox()
        Me.lstcls = New System.Windows.Forms.ListBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.cmbclasse = New System.Windows.Forms.ComboBox()
        Me.txtaggiungiclasse = New System.Windows.Forms.TextBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.BTNAGGCLS = New System.Windows.Forms.Button()
        Me.txtnome = New System.Windows.Forms.TextBox()
        Me.txtggassenza = New System.Windows.Forms.TextBox()
        Me.Button2 = New System.Windows.Forms.Button()
        Me.Button1 = New System.Windows.Forms.Button()
        Me.Button3 = New System.Windows.Forms.Button()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.Label8 = New System.Windows.Forms.Label()
        Me.txtnomealunno = New System.Windows.Forms.TextBox()
        Me.txtgiorni = New System.Windows.Forms.TextBox()
        Me.lbl = New System.Windows.Forms.Label()
        Me.Label9 = New System.Windows.Forms.Label()
        Me.Button4 = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'lstnm
        '
        Me.lstnm.FormattingEnabled = True
        Me.lstnm.Location = New System.Drawing.Point(84, 34)
        Me.lstnm.Name = "lstnm"
        Me.lstnm.Size = New System.Drawing.Size(166, 342)
        Me.lstnm.TabIndex = 0
        '
        'lstGa
        '
        Me.lstGa.FormattingEnabled = True
        Me.lstGa.Location = New System.Drawing.Point(256, 34)
        Me.lstGa.Name = "lstGa"
        Me.lstGa.Size = New System.Drawing.Size(166, 342)
        Me.lstGa.TabIndex = 1
        '
        'lstcls
        '
        Me.lstcls.FormattingEnabled = True
        Me.lstcls.Location = New System.Drawing.Point(16, 34)
        Me.lstcls.Name = "lstcls"
        Me.lstcls.Size = New System.Drawing.Size(62, 342)
        Me.lstcls.TabIndex = 3
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(23, 11)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(48, 13)
        Me.Label1.TabIndex = 4
        Me.Label1.Text = "CLASSE"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(130, 11)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(75, 13)
        Me.Label2.TabIndex = 5
        Me.Label2.Text = "NOMINATIVO"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(298, 11)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(98, 13)
        Me.Label4.TabIndex = 7
        Me.Label4.Text = "GIORNI ASSENZE"
        '
        'cmbclasse
        '
        Me.cmbclasse.FormattingEnabled = True
        Me.cmbclasse.Location = New System.Drawing.Point(75, 460)
        Me.cmbclasse.Name = "cmbclasse"
        Me.cmbclasse.Size = New System.Drawing.Size(132, 21)
        Me.cmbclasse.TabIndex = 8
        Me.cmbclasse.Text = "SELEZIONA CLASSE"
        '
        'txtaggiungiclasse
        '
        Me.txtaggiungiclasse.Location = New System.Drawing.Point(284, 455)
        Me.txtaggiungiclasse.Name = "txtaggiungiclasse"
        Me.txtaggiungiclasse.Size = New System.Drawing.Size(100, 20)
        Me.txtaggiungiclasse.TabIndex = 9
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label3.Location = New System.Drawing.Point(247, 430)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(175, 20)
        Me.Label3.TabIndex = 10
        Me.Label3.Text = "AGGIUNGI CLASSE"
        '
        'BTNAGGCLS
        '
        Me.BTNAGGCLS.Location = New System.Drawing.Point(267, 481)
        Me.BTNAGGCLS.Name = "BTNAGGCLS"
        Me.BTNAGGCLS.Size = New System.Drawing.Size(134, 23)
        Me.BTNAGGCLS.TabIndex = 11
        Me.BTNAGGCLS.Text = "AGGIUNGI CLASSE"
        Me.BTNAGGCLS.UseVisualStyleBackColor = True
        '
        'txtnome
        '
        Me.txtnome.Location = New System.Drawing.Point(75, 487)
        Me.txtnome.Name = "txtnome"
        Me.txtnome.Size = New System.Drawing.Size(132, 20)
        Me.txtnome.TabIndex = 12
        '
        'txtggassenza
        '
        Me.txtggassenza.Location = New System.Drawing.Point(75, 513)
        Me.txtggassenza.Name = "txtggassenza"
        Me.txtggassenza.Size = New System.Drawing.Size(132, 20)
        Me.txtggassenza.TabIndex = 13
        '
        'Button2
        '
        Me.Button2.Location = New System.Drawing.Point(75, 539)
        Me.Button2.Name = "Button2"
        Me.Button2.Size = New System.Drawing.Size(132, 23)
        Me.Button2.TabIndex = 14
        Me.Button2.Text = "AGGIUNGI DATI ALUNNO"
        Me.Button2.UseVisualStyleBackColor = True
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(16, 382)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(120, 23)
        Me.Button1.TabIndex = 15
        Me.Button1.Text = "CERCA MASSIMO"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'Button3
        '
        Me.Button3.Location = New System.Drawing.Point(142, 382)
        Me.Button3.Name = "Button3"
        Me.Button3.Size = New System.Drawing.Size(120, 23)
        Me.Button3.TabIndex = 16
        Me.Button3.Text = "MEDIA"
        Me.Button3.UseVisualStyleBackColor = True
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(5, 490)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(33, 13)
        Me.Label5.TabIndex = 17
        Me.Label5.Text = "nome"
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Location = New System.Drawing.Point(5, 516)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(61, 13)
        Me.Label6.TabIndex = 18
        Me.Label6.Text = "gg assenza"
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label7.Location = New System.Drawing.Point(68, 430)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(146, 20)
        Me.Label7.TabIndex = 19
        Me.Label7.Text = "AGGIUNGI DATI"
        '
        'Label8
        '
        Me.Label8.AutoSize = True
        Me.Label8.Location = New System.Drawing.Point(241, 458)
        Me.Label8.Name = "Label8"
        Me.Label8.Size = New System.Drawing.Size(37, 13)
        Me.Label8.TabIndex = 20
        Me.Label8.Text = "classe"
        '
        'txtnomealunno
        '
        Me.txtnomealunno.Location = New System.Drawing.Point(618, 212)
        Me.txtnomealunno.Name = "txtnomealunno"
        Me.txtnomealunno.Size = New System.Drawing.Size(100, 20)
        Me.txtnomealunno.TabIndex = 21
        '
        'txtgiorni
        '
        Me.txtgiorni.Location = New System.Drawing.Point(618, 169)
        Me.txtgiorni.Name = "txtgiorni"
        Me.txtgiorni.Size = New System.Drawing.Size(100, 20)
        Me.txtgiorni.TabIndex = 22
        '
        'lbl
        '
        Me.lbl.AutoSize = True
        Me.lbl.Location = New System.Drawing.Point(508, 172)
        Me.lbl.Name = "lbl"
        Me.lbl.Size = New System.Drawing.Size(104, 13)
        Me.lbl.TabIndex = 23
        Me.lbl.Text = "GIORNI TOT ANNO"
        '
        'Label9
        '
        Me.Label9.AutoSize = True
        Me.Label9.Location = New System.Drawing.Point(508, 212)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(66, 13)
        Me.Label9.TabIndex = 24
        Me.Label9.Text = "STUDENTE"
        '
        'Button4
        '
        Me.Button4.Location = New System.Drawing.Point(618, 255)
        Me.Button4.Name = "Button4"
        Me.Button4.Size = New System.Drawing.Size(75, 23)
        Me.Button4.TabIndex = 25
        Me.Button4.Text = "VERIFICA"
        Me.Button4.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(770, 586)
        Me.Controls.Add(Me.Button4)
        Me.Controls.Add(Me.Label9)
        Me.Controls.Add(Me.lbl)
        Me.Controls.Add(Me.txtgiorni)
        Me.Controls.Add(Me.txtnomealunno)
        Me.Controls.Add(Me.Label8)
        Me.Controls.Add(Me.Label7)
        Me.Controls.Add(Me.Label6)
        Me.Controls.Add(Me.Label5)
        Me.Controls.Add(Me.Button3)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.Button2)
        Me.Controls.Add(Me.txtggassenza)
        Me.Controls.Add(Me.txtnome)
        Me.Controls.Add(Me.BTNAGGCLS)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.txtaggiungiclasse)
        Me.Controls.Add(Me.cmbclasse)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.lstcls)
        Me.Controls.Add(Me.lstGa)
        Me.Controls.Add(Me.lstnm)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents lstnm As System.Windows.Forms.ListBox
    Friend WithEvents lstGa As System.Windows.Forms.ListBox
    Friend WithEvents lstcls As System.Windows.Forms.ListBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents cmbclasse As System.Windows.Forms.ComboBox
    Friend WithEvents txtaggiungiclasse As System.Windows.Forms.TextBox
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents BTNAGGCLS As System.Windows.Forms.Button
    Friend WithEvents txtnome As System.Windows.Forms.TextBox
    Friend WithEvents txtggassenza As System.Windows.Forms.TextBox
    Friend WithEvents Button2 As System.Windows.Forms.Button
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents Button3 As System.Windows.Forms.Button
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents Label7 As System.Windows.Forms.Label
    Friend WithEvents Label8 As System.Windows.Forms.Label
    Friend WithEvents txtnomealunno As System.Windows.Forms.TextBox
    Friend WithEvents txtgiorni As System.Windows.Forms.TextBox
    Friend WithEvents lbl As System.Windows.Forms.Label
    Friend WithEvents Label9 As System.Windows.Forms.Label
    Friend WithEvents Button4 As System.Windows.Forms.Button

End Class
