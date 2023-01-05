<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form esegue l'override del metodo Dispose per pulire l'elenco dei componenti.
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

    'Richiesto da Progettazione Windows Form
    Private components As System.ComponentModel.IContainer

    'NOTA: la procedura che segue è richiesta da Progettazione Windows Form
    'Può essere modificata in Progettazione Windows Form.  
    'Non modificarla nell'editor del codice.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.dgvdati = New System.Windows.Forms.DataGridView()
        Me.Button1 = New System.Windows.Forms.Button()
        CType(Me.dgvdati, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'dgvdati
        '
        Me.dgvdati.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.dgvdati.Location = New System.Drawing.Point(12, 16)
        Me.dgvdati.Name = "dgvdati"
        Me.dgvdati.RowTemplate.Height = 28
        Me.dgvdati.Size = New System.Drawing.Size(877, 473)
        Me.dgvdati.TabIndex = 0
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(126, 561)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(45, 30)
        Me.Button1.TabIndex = 1
        Me.Button1.Text = "Button1"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(9.0!, 20.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1294, 666)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.dgvdati)
        Me.Name = "Form1"
        Me.Text = "Form1"
        CType(Me.dgvdati, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub
    Friend WithEvents dgvdati As System.Windows.Forms.DataGridView
    Friend WithEvents Button1 As System.Windows.Forms.Button

End Class
